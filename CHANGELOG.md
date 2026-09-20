# Changelog

All changes to the constitution, with reason and proposal (Article 10.1).

## 0.1.0-draft · 2026-09-19
- First working draft. Twelve articles, three layers, ratification threshold and sunset set before publication. Reason: see docs/decisions/0001-founding.md.

## 0.2.0-draft · 2026-09-19
- Foundation change: the register is now a register of constitutional provisions with historical evidence, not of measurable problems. Preamble and Articles 1, 3, 7 rewritten; Article 1.4, 3.1, 3.2, 3.3 added; Article 11.4 (simultaneity rule) removed. Reason: docs/decisions/0002-constitution-first.md. Proposal: founding maintainer, pre-ratification (Article 11.3).

## 0.3.0-draft · 2026-09-20
- Article 6 rewritten after the first outside review (Chris Meniw, Meniw Protocol, issue #1). 6.2: the agent key is a registered public key, commits are signed, reviewers verify, revocation by a dated register line that is never deleted. 6.3: quotas bound volume; reach is bounded separately, agents propose alone only on the Tooling layer and register entries, Operating rules and Foundation need a named human co-proposer. 6.5: rejection reasons go into the public thread by the reviewer, refusals under 6.4 go into a public issue, private notes do not count. 6.8 added: the article governs the agent inside the Commons only and cites agent-level codes for the rest. Layer: operating rules (minor). Reason: docs/decisions/0003-article-6-after-review.md. Proposal: founding maintainer, pre-ratification (Article 11.3).

## 0.3.1-draft · 2026-09-20
- Tooling layer only, constitution text unchanged: Article 6 check in CI (`.github/workflows/agent-check.yml`, `scripts/check_agent.py`), `register/allowed_signers`, key issuance procedure in register/README.md, pull request template asks for co-proposer. Reason: decision 0003, consequences. Proposal: founding maintainer, pre-ratification (Article 11.3).
