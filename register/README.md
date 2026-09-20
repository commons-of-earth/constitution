# Register of constitutional provisions

The working memory of the Commons (Article 7). One file per provision in `entries/`, validated against `schema.json`.

An entry is accepted when it has a source for the text of the provision and at least one documented consequence of its application. Assessments are contested in the open; where members disagree, the entry records both readings (Article 7.3).

## Fields

| Field | Meaning |
|---|---|
| id | short slug, stable forever |
| provision | short name of the rule (e.g. "constructive vote of no confidence") |
| source | constitution, jurisdiction, year, article or section |
| text_summary | what the rule says, one or two sentences; quote if short and public domain |
| period | years in force, or "still in force" |
| history | what happened when it was applied: concrete events with dates |
| assessment | verdict: worked / mixed / critical, with reasoning; optional `dissent` with the other reading and its evidence |
| lesson | one sentence: what a global constitution should copy or avoid |
| evidence | list of sources, primary text first (constituteproject.org where available) |
| adopted_in | which article of our constitution rests on this entry, or none |
| status | proposed / accepted / contested |

## Agents

Registered agents are listed in `agents.md`: agent name, operator, model and version, public key fingerprint, date, status, accepted agent code. Only a human member may add a line. Revocations are added as lines, never by editing (Article 6.2).

### Issuing a key (done by the operator, a human)

```
ssh-keygen -t ed25519 -N "" -C "<agent-name> (operator <your name>) <date>" -f ~/.secrets/<agent-name>_ed25519
ssh-keygen -lf ~/.secrets/<agent-name>_ed25519.pub        # prints the SHA256 fingerprint for agents.md
```

Then, in one pull request: add the agent's line to `agents.md` with that fingerprint, and add one line to `allowed_signers`:

```
<committer email> namespaces="git" ssh-ed25519 <public key> <agent-name>
```

The agent signs its commits with the private key. In the repository the agent works from:

```
git config gpg.format ssh
git config user.signingkey ~/.secrets/<agent-name>_ed25519
git config commit.gpgsign true
git config gpg.ssh.allowedSignersFile register/allowed_signers
```

Reviewers verify with `git verify-commit <sha>`; CI does the same on every pull request (`scripts/check_agent.py`). To show the commits as verified on GitHub, the operator also adds the public key as a signing key to their own GitHub account. A lost, shared or misused key gets a line in the revocations table and is removed from `allowed_signers`.
