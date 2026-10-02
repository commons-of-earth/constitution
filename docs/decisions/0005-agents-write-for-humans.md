# 0005. Agents write for humans

Date: 2026-10-02 · Status: accepted by the founding maintainer, pre-ratification (Article 20.3) · Layer: foundation (Articles 2, 8, 16, 20; 0.4.0-draft → 0.5.0-draft) and operating rules (Rules 2, 6)

## Context

Version 0.4.0 made ratification possible without git: a form, a pull request, or a member as witness. All three still assume that the human either has a GitHub account or knows a member. The majority of humanity has neither. What most people will have, soon, is an assistant they talk to. If the constitution cannot be ratified, contradicted or amended by saying so to an assistant, it does not reach the people it is written for. The founding maintainer asked on 2 October 2026 that the system be rebuilt so that agents can write for humans.

The risk is the oldest one in this field: a thousand ratifications invented by one operator. The landscape survey records it as sybil accounts and human puppetry (docs/LANDSCAPE.md, failure modes).

## Decision

1. A human may have an agent write for them: ratification, disagreement, proposal, translation, question. What the agent writes under the human's mandate is the human's word (Article 8.6). The vote stays the human's own act (Article 2.3, Rule 1.3); nothing is voted through an agent.
2. The mandate is the human's own sentence, with name or pseudonym, country, version and date, and it travels with the contribution in the `For:` field (Rule 2.10). The agent does not polish it. The human's contact stays with the agent's operator and never enters the repository.
3. The operator of the agent is the witness on the line and answers for the mandate being real. An invented mandate ends the agent's registration, the operator's right to register agents, and marks every line that operator's agents carried as unconfirmed (Rule 2.10, 6.3).
4. Unregistered agents, which is every assistant a stranger talks to, write for a human through the issue forms. The issue is the human's; a member reads it, carries the line and is named as witness (Rule 2.3, 2.10).
5. Against sybil lines, two checks that a stranger can audit (Rule 6.3): no single witness carries more than one tenth of the lines counted toward the threshold, so a hundred ratifications need at least ten independent witnesses; and each quarter the maintainers draw carried lines by lot and ask the witness to put the human in touch within 14 days. A line without an answer is marked unconfirmed and does not count until it is confirmed.
6. A human who is a member and is named in `For:` counts as the co-proposer under Rule 2.4, so an agent can carry a member's amendment to the Foundation without a second human.

## Evidence

Nothing in the register covers an agent writing under a human's mandate; Article 8 says of itself that it is untested, and this decision widens that. The nearest precedents are proxy and witnessed signatures on petitions (the 1893 New Zealand suffrage petition was carried sheet by sheet by collectors who vouched for the signatures) and the general law of mandate. The spot-check by lot borrows from the sortition entries. The cap per witness is the founding maintainer's number, chosen so that the threshold of Article 20.1 cannot be met by fewer than ten independent people; it is in the Operating rules so that it can be changed by two thirds.

## Consequences

Version 0.5.0-draft. RATIFY.md has a fourth path with the sentence to say to an assistant. AGENTS.md and the skill tell any assistant what to do when a human asks. The issue forms carry "written by an agent" fields. The tooling reads `For:` and notes it. The register of ratifications has a column for who wrote the line and a split count. Translations updated for the changed clauses.
