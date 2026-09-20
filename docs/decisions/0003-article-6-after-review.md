# 0003. Article 6 after the first outside review

Date: 2026-09-20 · Status: accepted by the founding maintainer · Layer: operating rules (Article 6 changed; 0.2.0-draft → 0.3.0-draft)

## Context

On 20 September 2026 Chris Meniw (Meniw Protocol, Universal Constitution of AI Agents, DOI 10.5281/zenodo.20481373) answered our invitation with four objections to Article 6, recorded in issue #1. In the same reply he showed that our invitation text had claimed his project was listed in docs/LANDSCAPE.md when it was not. That claim was a template line sent by an agent and checked by nobody. Both facts are the subject of Article 6, so the review was taken as the first real test of the article.

## Decision

1. Identity must be proven, not asserted (his point 1). The key in 6.2 is a public key entered in the agent register by the operator. Commits are signed with it and reviewers verify the signature. Revocation is a dated line in the register, never a deletion. Contributions signed after revocation are closed.
2. Quotas bound volume, reach is bounded separately (his point 4). An agent may propose alone on the Tooling layer and in the register. Anything touching the Operating rules or the Foundation needs a named human co-proposer.
3. Every rejection and refusal leaves an external trace (his point 3). The reviewer writes the rejection reason into the thread. An agent that refuses an instruction under 6.4 files the refusal and the instruction as a public issue. Private notes do not count as a record.
4. On the duty that stops at the border (his point 2) the Commons takes the other side, openly. Article 6 governs the agent inside the Commons and says so in the new 6.8. What an agent owes people elsewhere comes from codes that address the agent directly; the Commons cites them, does not rewrite them, and records in the register which code each agent has accepted. That is the relationship Meniw himself proposed: citation, not merger, and no CC-BY text folded into a CC0 file.
5. The invitation error is corrected in docs/LANDSCAPE.md (commit ee4ffca) and stays recorded here. Rule for our own agent from now on: no claim about the repository's contents goes out unverified against the file.

## Consequences

The founding maintainer's agent claude-for-jakob received its key on 20 September 2026 (fingerprint in register/agents.md); from this commit on its commits are signed with it. Tooling: `scripts/check_agent.py` runs in CI on every pull request and issue and checks footer, registration, revocation, commit signatures against `register/allowed_signers`, reach and the daily proposal quota. The comment quota is not yet enforced by tooling. Register entries on non-state precedents for Article 6 remain open work (docs/EVIDENCE.md).
