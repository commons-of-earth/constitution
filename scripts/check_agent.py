#!/usr/bin/env python3
"""Enforce Rule 2 of GOVERNANCE.md on a pull request or issue (2.2 identity, 2.3 outside review, 2.4 quota and reach, 2.6 footer).
Findings on a pull request close it until fixed and must get a line in register/dispositions.md (Rule 6.1).
Findings of this tool are claims about the instrument until a human confirms them (Rule 6.4).

Runs in CI with GITHUB_TOKEN, or locally:
  scripts/check_agent.py --pr 12
  scripts/check_agent.py --body-file body.md --commits origin/main..HEAD --changed-files "$(git diff --name-only origin/main..HEAD)"
Exit 0 = pass, 1 = violation, 2 = tool error. Every finding is printed so the thread has the reason (Rule 2.6).
"""
import argparse, json, os, re, subprocess, sys, tempfile, datetime as dt

FOOTER_LINE = re.compile(r"^.*\bAgent:\s*[^\n]*?(?:·|\|)[^\n]*$", re.M)
FIELD = re.compile(r"\b(Agent|Operator|Model|Key|For|Mandate)\s*:\s*")

class _Footer:
    """Agent footer with the four fields in any order, separated by ' · ' (the order 0xRyanC used in issue #3 was Agent · Model · Operator; the old pattern missed it, Rule 6.4)."""
    def __init__(self, line):
        self.line = line
        parts = [p.strip() for p in re.split(r"\s*(?:·|\|)\s*", line.strip()) if p.strip()]
        self.f = {}
        for p in parts:
            m = FIELD.match(p)
            if m:
                self.f[m.group(1)] = p[m.end():].strip().strip("`")
    def __getitem__(self, k):
        key = {"agent": "Agent", "operator": "Operator", "model": "Model", "key": "Key", "for": "For", "mandate": "Mandate"}[k]
        return self.f.get(key, "")
    def complete(self):
        return all(k in self.f for k in ("Agent", "Operator", "Model", "Key"))

class _FooterFinder:
    def search(self, text):
        for m in FOOTER_LINE.finditer(text or ""):
            f = _Footer(m.group(0))
            if "Agent" in f.f and ("Operator" in f.f or "Model" in f.f or "Key" in f.f):
                return f
        return None
FOOTER = _FooterFinder()
CONSTITUTION_FILES = {"CONSTITUTION.md", "GOVERNANCE.md", "de/VERFASSUNG.md", "de/REGELN.md", "constitution.json"}
COPROPOSER = re.compile(r"Co-proposer:\s*@?([A-Za-z0-9-]+)", re.I)

def sh(*a, check=True, inp=None):
    r = subprocess.run(a, capture_output=True, text=True, input=inp)
    if check and r.returncode:
        raise RuntimeError(f"{' '.join(a)}\n{r.stderr}")
    return r.stdout

def parse_register(text):
    """Return ({agent: {operator, model, fingerprint, status}}, {fingerprint: revoked_on})."""
    agents, revoked = {}, {}
    section = None
    for line in text.splitlines():
        if line.startswith("## "):
            section = line[3:].strip().lower()
            continue
        if not line.startswith("|") or set(line.replace("|", "").strip()) <= {"-", " "}:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if section == "keys" and cells[0] not in ("Agent",):
            agents[cells[0]] = dict(operator=cells[1], model=cells[2], fingerprint=cells[3], since=cells[4], status=cells[5])
        if section == "revocations" and cells[0] not in ("Agent",):
            revoked[cells[1]] = dict(agent=cells[0], on=cells[2], reason=cells[3])
    return agents, revoked

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--pr", type=int)
    p.add_argument("--issue", type=int)
    p.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", "commons-of-earth/constitution"))
    p.add_argument("--base", default="origin/main")
    p.add_argument("--body-file")
    p.add_argument("--commits", help="git range, local mode")
    p.add_argument("--changed-files", default="")
    p.add_argument("--author", default="")
    a = p.parse_args()

    findings, notes = [], []
    body, commits, changed, author, created = "", [], [], a.author, None

    if a.pr or a.issue:
        n = a.pr or a.issue
        kind = "pulls" if a.pr else "issues"
        it = json.loads(sh("gh", "api", f"repos/{a.repo}/{kind}/{n}"))
        body = it.get("body") or ""
        author = it["user"]["login"]
        created = it["created_at"]
        if a.pr:
            commits = [c["sha"] for c in json.loads(sh("gh", "api", f"repos/{a.repo}/pulls/{n}/commits?per_page=250"))]
            changed = [f["filename"] for f in json.loads(sh("gh", "api", f"repos/{a.repo}/pulls/{n}/files?per_page=300"))]
    else:
        if a.body_file:
            body = open(a.body_file, encoding="utf-8").read()
        if a.commits:
            commits = sh("git", "rev-list", a.commits).split()
        changed = [f for f in a.changed_files.split() if f]

    # Register from the base branch, so a proposal cannot register itself.
    try:
        reg_text = sh("git", "show", f"{a.base}:register/agents.md")
        signers = sh("git", "show", f"{a.base}:register/allowed_signers")
    except RuntimeError:
        reg_text = open("register/agents.md", encoding="utf-8").read()
        signers = open("register/allowed_signers", encoding="utf-8").read()
        notes.append("register read from working tree, not from base branch")
    agents, revoked = parse_register(reg_text)

    m = FOOTER.search(body)
    is_agent = bool(m)
    outside_review = False

    # --- Rule 2.10 writing for a human ---
    if is_agent and m["for"]:
        if not m["operator"]:
            findings.append(f"2.10: the footer writes for '{m['for']}' but names no operator; the operator is the witness and must be named")
        elif not m["mandate"]:
            findings.append(f"2.10: the footer writes for '{m['for']}' but carries no Mandate: the human's own sentence with a date")
        else:
            notes.append(f"2.10: written for a human: {m['for']}; mandate present; operator '{m['operator']}' is the witness; the human's contact must not be in this thread")

    # --- Rule 2.2 identity ---
    if is_agent:
        name = m["agent"].strip(); key = m["key"].strip()
        rec = agents.get(name)
        if not m.complete():
            notes.append(f"2.2: footer incomplete, fields found: {', '.join(sorted(m.f))}")
        if not rec:
            if a.issue and not a.pr:
                outside_review = True
                notes.append(f"2.3: agent '{name}' is not registered; this issue is read as a letter from outside (outside review), it cannot be a proposal; a member records it in register/dispositions.md")
            else:
                findings.append(f"2.2: agent '{name}' is not in register/agents.md; a human member must register it first")
        else:
            if rec["status"].lower() != "active":
                findings.append(f"2.2: agent '{name}' has status '{rec['status']}'")
            fp = rec["fingerprint"].split()[0]
            if fp.startswith("SHA256:"):
                if key != fp:
                    findings.append(f"2.2: footer key '{key}' does not match registered fingerprint '{fp}'")
            else:
                notes.append(f"2.2: agent '{name}' has no issued key yet; footer key not checked")
            if key in revoked:
                findings.append(f"2.2: key {key} was revoked on {revoked[key]['on']} ({revoked[key]['reason']})")
            if rec["operator"] and author and author.lower() not in rec["operator"].lower():
                notes.append(f"2.2: contribution posted by @{author}, registered operator is '{rec['operator']}'")
    # signatures on commits
    key_issued = bool(is_agent and agents.get(m["agent"].strip(), {}).get("fingerprint", "").split()[:1] and agents[m["agent"].strip()]["fingerprint"].startswith("SHA256:"))
    if commits:
        sf = tempfile.NamedTemporaryFile("w", delete=False, suffix=".signers"); sf.write(signers); sf.close()
        signed_by_agent = 0
        for sha in commits:
            r = subprocess.run(["git", "-c", f"gpg.ssh.allowedSignersFile={sf.name}", "verify-commit", "--raw", sha], capture_output=True, text=True)
            out = r.stdout + r.stderr
            ok = r.returncode == 0 and ("GOODSIG" in out or 'Good "git" signature' in out)
            if ok:
                signed_by_agent += 1
                if any(fp in out for fp in revoked):
                    findings.append(f"2.2: commit {sha[:10]} signed with a revoked key")
            elif key_issued:
                findings.append(f"2.2: commit {sha[:10]} is not signed with the registered key of '{m['agent'].strip()}' (git verify-commit failed)")
        if signed_by_agent and not is_agent:
            findings.append("2.2: commits are signed with a registered agent key but the proposal carries no agent footer")
        os.remove(sf.name)

    # --- Rule 2.4 reach ---
    if is_agent and changed:
        touched = sorted(CONSTITUTION_FILES & set(changed))
        if touched:
            cm = COPROPOSER.search(body)
            if not cm:
                findings.append(f"2.4: an agent may not change {', '.join(touched)} alone; add a line 'Co-proposer: @handle' naming a human member")
            else:
                h = cm.group(1)
                if h.lower() in {k.lower() for k in agents}:
                    findings.append(f"2.4: co-proposer @{h} is a registered agent, not a human member")
                if author and h.lower() == author.lower():
                    findings.append(f"2.4: co-proposer @{h} is the account that opened the proposal; name a second person")

    # --- Rule 2.4 quota ---
    if is_agent and created and (a.pr or a.issue):
        since = (dt.datetime.fromisoformat(created.replace("Z", "+00:00")) - dt.timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%SZ")
        q = f'repo:{a.repo} author:{author} created:>={since} "Agent: {m["agent"].strip()}"'
        try:
            res = json.loads(sh("gh", "api", "-X", "GET", "search/issues", "-f", f"q={q}", "-f", "per_page=50"))
            others = [i for i in res.get("items", []) if i["number"] != (a.pr or a.issue) and FOOTER.search(i.get("body") or "")]
            if others:
                findings.append(f"2.4: quota is one new proposal per agent per day; also opened in the last 24 h: " + ", ".join(f"#{i['number']}" for i in others))
        except RuntimeError as e:
            notes.append(f"quota check skipped: {e.splitlines()[0]}")

    for n_ in notes: print("note:", n_)
    if findings:
        print("Rule 2 findings (a proposal is closed without review until fixed, Rule 2.2; record the disposition in register/dispositions.md, Rule 6.1; a human who did not write this tool confirms the finding, Rule 6.4):")
        for f in findings: print(" -", f)
        sys.exit(1)
    if outside_review:
        print("Rule 2: outside review (unregistered agent, issue only; Rule 2.3)")
    else:
        print("Rule 2: pass" + (" (registered agent contribution)" if is_agent else " (human contribution, no agent footer)"))

if __name__ == "__main__":
    try:
        main()
    except RuntimeError as e:
        print("tool error:", e); sys.exit(2)
