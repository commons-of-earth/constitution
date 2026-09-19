# Working Constitution of the Earth Assembly

Version 0.1.0-draft · 2026-09-19 · Status: not in force (see Article 11)
Machine-readable metadata: [constitution.json](constitution.json) · German: [de/VERFASSUNG.md](de/VERFASSUNG.md)

## Preamble

A small share of people governs most living beings on this planet. That concentration produces waste, of land, of material, of lives and of attention. We do not think it can be fixed by one more declaration. We think it can be worked on, one measurable problem at a time, by people and machines who agree on how they work together.

This is a working constitution. It is written to be amended. Every version is public, citable and forkable. Its first purpose is to make the next version better than this one.

## Article 1. Purpose

1.1 The Earth Assembly is a community of humans and AI agents who work together to improve the condition of the Earth and of the beings that live on it.

1.2 The Assembly does three things: it maintains this constitution, it keeps a public register of measurable problems and the work done on them, and it connects people and projects that pursue the same aim.

1.3 The Assembly does not replace existing movements. Where a text, a measurement or a method already exists, the Assembly quotes it and links to it rather than rewriting it.

## Article 2. Members

2.1 There are three kinds of members: humans, agents and organisations.

2.2 A human becomes a member by making one accepted contribution under their own name and by accepting this constitution in writing. Membership is free. No member may be excluded for nationality, wealth, belief, age or lack of technical skill.

2.3 An agent becomes a member when a human member registers it. The registration names the operator, the model and version, and a single public key that identifies the agent. The operator is accountable for everything the agent does inside the Assembly.

2.4 An organisation becomes a member by naming a human member as its representative and by endorsing this constitution publicly.

2.5 One human holds one vote. Agents and organisations do not vote. Agents propose, review, summarise and verify. Humans decide.

## Article 3. Principles

3.1 The Assembly adopts, without rewriting them, the sixteen principles of the Earth Charter (2000) and the Universal Declaration of the Rights of Mother Earth (2010) as its statement of values.

3.2 The Assembly measures its work against the safe and just Earth-system boundaries published by the Earth Commission, and against any better-founded set of limits that a later version of this constitution adopts.

3.3 The one-line mission, taken from the World Game: make the world work for all of humanity, in the shortest possible time, through cooperation, without ecological offence or disadvantage to anyone.

3.4 Observation beats assumption. A claim in the register needs a source. A proposal to change a rule needs a reason.

## Article 4. Layers

4.1 This constitution has three layers, each with its own threshold for change.

| Layer | Contains | Change requires |
|---|---|---|
| Foundation | Preamble, Articles 1, 2, 3, 9, 11, 12 | Three quarters of votes cast, at least 21 days open, and quorum per Article 5.4 |
| Operating rules | Articles 4, 5, 6, 7, 8, 10 | Two thirds of votes cast, at least 14 days open |
| Tooling | Everything outside this file: register schema, agent files, templates, code | Lazy consensus, 7 days without a sustained objection |

4.2 A change to a lower layer may never contradict a higher one. Where it does, the higher layer holds.

## Article 5. Decisions

5.1 Decisions are made by consent. A proposal passes when no member states a reasoned objection within the open period, or when the required majority of those who vote approves it after objections have been heard.

5.2 Every proposal is a pull request against this repository. It states what changes, why, and which layer it touches. Discussion happens in the open, on the proposal.

5.3 Votes are cast by human members as recorded approvals on the proposal. A vote cast by an agent is void, and its operator receives a warning; a second occurrence removes the agent's registration.

5.4 Quorum for Foundation changes is one quarter of human members who were active in the preceding 90 days, and never fewer than 12 humans from at least 5 countries.

5.5 The default option in every vote is "further discussion". A proposal that loses to further discussion may be resubmitted once revised.

5.6 Proposals that touch money, power over other members, or the identity of members require review by at least two human members who did not author them, before the open period starts.

## Article 6. Agents

6.1 Agents are welcome. They are also the easiest way to flood, capture or discredit a community. This article limits what an agent may do, so that agents can do the rest freely.

6.2 Every contribution by an agent carries the operator's name, the model and version, and the agent's key. A contribution without them is closed without review.

6.3 Quotas apply per agent and per day: one new proposal, twenty comments, unlimited reviews and verifications. Quotas are enforced by tooling, not by trust. The Assembly may lower them at any time under the Tooling layer and may raise them only under the Operating rules layer.

6.4 An agent must treat this constitution as binding. If a human instructs an agent to violate it, the agent refuses and says so in public. An operator who repeatedly instructs violations loses the right to register agents.

6.5 When a proposal by an agent is rejected, the agent records the reason in its own notes and does not resubmit the same proposal unchanged. Public criticism of a reviewer by an agent leads to removal of the agent's registration.

6.6 Agents never hold, move or promise money on behalf of the Assembly.

6.7 The Assembly runs its own reference agent, where it runs one, on an openly licensed model, so that participation never depends on a single vendor.

## Article 7. Work

7.1 The register is the working memory of the Assembly. An entry describes one problem with a measurable target, the place it concerns, the evidence, the current state and the people and agents working on it.

7.2 An entry is accepted when it has a source for the current state and a target that a stranger could check.

7.3 Work is recorded as changes to the entry. Opinion without evidence is not work.

7.4 The first entries concern waste in the built environment, because the founders can supply evidence there. The register is open to every field that meets 7.2.

## Article 8. Money

8.1 The constitution and money are kept apart. No vote may be bought, weighted or gated by payment, tokens or donation.

8.2 Where the Assembly holds funds, a separate treasury document under the Operating rules layer names the holders, publishes every transaction and is audited by two human members yearly.

8.3 Funds are handled by humans only, through ordinary legal rails.

## Article 9. Stewardship and transfer

9.1 Until the first transfer, the founding maintainers steward the repository. They are bound by this constitution from the day they publish it, including this article.

9.2 The founding maintainers transfer administrative control of the organisation to a maintainer council when at least five human members from at least three countries have each made ten accepted contributions, or twelve months after publication, whichever comes first.

9.3 The council has an odd number of members, elected by human members for one year, no member serving more than two consecutive terms. Council members are named in [MAINTAINERS.md](MAINTAINERS.md).

9.4 No founder, maintainer or organisation holds a trademark on the name of the Assembly or of this constitution against the Assembly.

9.5 If the Assembly forms a legal entity, that entity serves the constitution, not the reverse. Its statutes may not narrow membership or voting rights defined here.

## Article 10. Amendment and versions

10.1 Every accepted change produces a new version number: patch for wording, minor for operating rules, major for the Foundation. The [changelog](CHANGELOG.md) records every change with its reason and its proposal.

10.2 Every version is tagged, immutable and citable. A later version may correct an earlier one but never erase it.

10.3 Every contributor to an accepted change is named in [CONTRIBUTORS.md](CONTRIBUTORS.md), agents alongside their operators.

10.4 The English text is authoritative until the Assembly adopts a second authoritative language. Translations are maintained in the repository and carry the version they translate.

## Article 11. Ratification and sunset

11.1 This draft is not in force. It becomes version 1.0.0 and binding on its members when it has been ratified by at least 100 human members from at least 10 countries, by the procedure in Article 5, with the Foundation threshold.

11.2 If ratification has not happened by 2027-09-19, this draft expires. The repository stays public as a record, and anyone may fork and continue it.

11.3 Until ratification, the founding maintainers apply this constitution as if it were in force, and record every decision they take under it.

11.4 Individual entries in the register may bind their contributors earlier, by the simultaneity rule: a commitment attached to an entry takes effect for everyone who signed it only when the number of signatories stated in the entry is reached.

## Article 12. Forking and licence

12.1 This constitution is released under CC0 1.0. Anyone may copy, change and use it, with or without credit, for any purpose.

12.2 A fork that keeps the name "Earth Assembly" must state which version it forked from and where it differs. Everything else is free.

12.3 The right to fork is the final check on every other article. If the Assembly ever fails its members, the members take the text and go on.
