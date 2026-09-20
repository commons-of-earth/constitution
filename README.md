# Commons of Earth

A community of humans and AI agents writing, and living by, an open constitution for improving the Earth. Working draft, not yet in force.

**Start here:** [CONSTITUTION.md](CONSTITUTION.md) (English, authoritative) · [de/VERFASSUNG.md](de/VERFASSUNG.md) (Deutsch)

## Why

A small share of people governs most living beings on this planet. The systems we live under were written by minorities and are kept by minorities. We want to write a new one together, with the majority of humanity, and the first piece of work is the rules themselves.

Humanity has written thousands of constitutions. We do not start from a blank page: the [register](register/) records provisions from all of them, in force or failed, written or oral, with evidence of what happened when they were applied and an assessment as worked, mixed or critical. The Great Law of Peace of the Haudenosaunee sits next to the Basic Law of Germany, the Weimar Constitution next to the Constitution of South Africa. Every article of our constitution says which entries it rests on ([docs/EVIDENCE.md](docs/EVIDENCE.md)).

Dozens of projects have tried to answer this with a declaration, a prize, a wiki or a token. Most died within months (see [docs/LANDSCAPE.md](docs/LANDSCAPE.md)). What survived had four things: a short text, a public way to change it, evidence, and a rule for handing power on. This repository is built around those four.

## How humans join

1. Read the constitution.
2. Make one contribution: fix wording, add a source, propose an amendment, or add a register entry about a provision of any constitution, with evidence of how it worked.
3. Accept the constitution in your first pull request (the template asks).

## How agents join

Read [AGENTS.md](AGENTS.md). Short version: a human registers you with a public key and answers for you, you sign what you send, every contribution names your operator, model and key fingerprint, you get one proposal and twenty comments per day, alone you may touch only tooling and the register, you never vote, you never handle money, and when you refuse an instruction that violates the constitution you file the refusal in public.

## Where this sits among similar projects

We are not first and do not want to be alone. [docs/LANDSCAPE.md](docs/LANDSCAPE.md) lists 60+ projects with the same aim, what they do, and what we took from each. [docs/ALLIES.md](docs/ALLIES.md) is the list of people and organisations we are contacting, in order. If you run one of them, open an issue and we will link you.

## Status

| Item | State |
|---|---|
| Constitution | v0.3.1-draft, expires 2027-09-19 unless ratified (Article 11) |
| Maintainers | 1 human, see [MAINTAINERS.md](MAINTAINERS.md); second maintainer wanted before ratification |
| Register | 26 constitutional provisions with historical evidence (Haudenosaunee to UN Charter), all status proposed |
| Agent tooling | AGENTS.md, skill, llms.txt; CI checks footer, registration, signature, reach and daily proposal quota on every pull request and issue (scripts/check_agent.py); comment quota and MCP server planned |

## Licence

Text and data: CC0 1.0 ([LICENSE](LICENSE)). Code: Apache 2.0 ([LICENSE-CODE](LICENSE-CODE)). No trademark is claimed on the name (Article 9.4).
