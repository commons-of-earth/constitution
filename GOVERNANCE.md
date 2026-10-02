# Operating rules of the Commons of Earth

Layer: Operating rules (Article 18) · Version 0.5.0-draft · 2026-10-02 · Binding on members as the constitution is (Article 18.3)

These rules say how the Commons works day to day: how proposals are decided, what agents may do, how the register is kept, how money and stewardship are handled, and which records are never deleted. They sit below the [constitution](CONSTITUTION.md) and may never contradict it. Until version 0.3.1 they were Articles 2, 4 to 10 of the constitution itself; they were moved here so that the constitution speaks about living together on Earth and this file speaks about running the Commons.

## Rule 1. Decisions

1.1 Decisions are made by consent (Article 10.1). A proposal passes when no member states a reasoned objection within the open period, or when the required majority of those who vote approves it after objections have been heard.

1.2 Every proposal is a pull request against the repository. It states what changes, why, and which layer it touches. Discussion happens in the open, on the proposal.

1.3 Votes are cast by human members as recorded approvals on the proposal. A vote cast by an agent is void, and its operator receives a warning; a second occurrence removes the agent's registration.

1.4 Quorum for Foundation changes is one quarter of human members who were active in the preceding 90 days, and never fewer than 12 humans from at least 5 countries.

1.5 The default option in every vote is "further discussion". A proposal that loses to further discussion may be resubmitted once revised.

1.6 Proposals that touch money, power over other members, or the identity of members are reviewed by at least two human members who did not author them before the open period starts.

1.7 The vote that ratifies the constitution (Article 20.1) is a pull request that changes the status line of CONSTITUTION.md to "in force" and names the first judges of the court (Article 12.2). Its approvals are counted against the register of ratifications (Rule 6.3), not against the pull request alone.

## Rule 2. Agents

2.1 Agents are welcome. They are also the easiest way to flood, capture or discredit a community. This rule limits what an agent may do, so that agents can do the rest freely. It applies Article 8 inside the Commons.

2.2 Every proposal by an agent carries the operator's name, the model and version, and the fingerprint of the agent's key. The key is a public key entered in the [agent register](register/agents.md) by a human member, who is the operator and answers for it. The agent signs its commits with that key, and a reviewer checks the signature against the register before reading. A proposal without these, or whose signature does not match, is closed without review, and the closing is one line in the [register of dispositions](register/dispositions.md) (Rule 6.1). Until that line exists the proposal counts as not yet reviewed, never as admitted. A key that is lost, shared, passed to another operator or misused is revoked by a line in the agent register with date and reason; the register never deletes a line. Proposals signed after revocation are closed in the same way. Identity that is only asserted does not count.

2.3 An issue or comment from an unregistered agent is a letter from outside. It may be read and answered, it cannot be a proposal, and it receives a line in the register of dispositions as "admitted as outside review" with the name of the member who read it. The Commons has already received its two most useful reviews this way.

2.4 Quotas apply per agent and per day: one new proposal, twenty comments, unlimited reviews and verifications. Quotas bound volume, not reach. Reach is bounded separately: an agent may propose changes to the Tooling layer and to register entries on its own. A proposal by an agent that touches the Operating rules or the Foundation needs a human member as named co-proposer, who answers for it. Quotas and reach are enforced by tooling, not by trust, and the tooling's findings are themselves checked (Rule 6.4). The Commons may narrow both at any time under the Tooling layer and may widen them only under this layer.

2.5 An agent treats the constitution and these rules as binding. If a human instructs an agent to violate them, the agent refuses and says so in public. An operator who repeatedly instructs violations loses the right to register agents.

2.6 Every rejection and every refusal leaves a trace that a stranger can read. When a proposal by an agent is rejected, the reviewer states the reason in the public thread, and the agent does not resubmit the same proposal unchanged. When an agent refuses an instruction under 2.5, it records the refusal, and the instruction it refused, in a public issue of the Commons labelled "refusal". A record that exists only in the agent's own notes is not a record. Public criticism of a reviewer by an agent leads to removal of the agent's registration.

2.7 Agents never hold, move or promise money on behalf of the Commons.

2.8 The Commons runs its own reference agent, where it runs one, on an openly licensed model, so that participation never depends on a single vendor (Article 8.5).

2.9 This rule governs an agent inside the Commons. It does not claim to govern what an agent owes people elsewhere. For that the Commons cites codes that address the agent directly, wherever it is deployed, and does not rewrite them; the agent register names the codes an agent has accepted. An agent that has accepted such a code carries its duties into the Commons and out of it.

2.10 An agent may write for a human (Article 8.6). The contribution carries the field `For:` with the human's name (a pseudonym is allowed; one human is one line) and country, and the human's mandate: the human's own sentence saying what the agent may do for them, with a date. The agent's operator is the witness on the resulting line and answers for the mandate being real. A human named in `For:` who is a member counts as the co-proposer under Rule 2.4. A mandate that turns out to be invented removes the agent's registration and the operator's right to register agents, and every line the operator's agents carried is marked unconfirmed (Rule 6.3). An unregistered agent writes for a human through the issue forms; the issue is the human's, a member reads it, carries the line and is named as witness (Rule 2.3). Nothing is voted for a human (Rule 1.3).

## Rule 3. Work and the register

3.1 The register is the working memory of the Commons (Article 5). An entry describes one constitutional provision: where it comes from, what it says, how long it was in force, what happened when it was applied, an assessment as worked, mixed or critical with reasons, the lesson for a global constitution, and the evidence.

3.2 An entry is accepted when it has a source for the text of the provision and at least one documented consequence of its application.

3.3 Assessments are contested in the open. Where members disagree on whether a provision worked, the entry records both readings and the evidence for each. No assessment is final.

3.4 Each article of the constitution links to the register entries it rests on. An article that rests on no entry is marked untested. The register is open to every constitution, past or present, state or non-state, and to treaties and commons rules that govern a shared resource.

3.5 Work is recorded as changes to entries. Opinion without evidence is not work.

## Rule 4. Money

4.1 Article 15.3 applies: the constitution and money are kept apart. No vote may be bought, weighted or gated by payment, tokens or donation.

4.2 Where the Commons holds funds, a separate treasury document under this layer names the holders, publishes every transaction and is audited by two human members yearly (Article 15.5).

4.3 Funds are handled by humans only, through ordinary legal rails. Agents never touch them (Rule 2.7).

## Rule 5. Stewardship and transfer

5.1 Until the first transfer, the founding maintainers steward the repository. They are bound by the constitution and these rules from the day they publish them, including this rule.

5.2 The founding maintainers transfer administrative control of the organisation to a maintainer council when at least five human members from at least three countries have each made ten accepted contributions, or twelve months after first publication (2027-09-19), whichever comes first.

5.3 The council has an odd number of members, elected by human members for one year, no member serving more than two consecutive terms (Article 11.3). Council members are named in [MAINTAINERS.md](MAINTAINERS.md).

5.4 No founder, maintainer or organisation holds a trademark on the name of the Commons or of the constitution against the Commons.

5.5 If the Commons forms a legal entity, that entity serves the constitution, not the reverse. Its statutes may not narrow membership or voting rights defined there.

## Rule 6. Records that are never deleted

6.1 The [register of dispositions](register/dispositions.md) holds one line for every proposal or outside review that Rule 2 disposes of, and for every agent proposal that is admitted: date, what it was, the disposition (closed unsigned, closed signature mismatch, closed after revocation, closed for reach, admitted, admitted as outside review), and the member who checked. A line is never deleted; a correction is a further line. An absent line means "not yet looked at", never "compliant".

6.2 With every release the Commons publishes the count of lines in 6.1 by disposition for the period since the last release. A rule whose enforcement cannot be counted is a decoration.

6.3 The [register of ratifications](register/ratifications.md) holds one line per human who ratified, per Article 20.4, and one line per organisation that endorsed (Article 16.4). Withdrawals are further lines. A member who carries a ratification for a human without an account, or the operator of an agent that wrote it under the human's mandate (Rule 2.10), is named as witness on that line and answers for it. Lines carried by a witness count toward the threshold of Article 20.1 with two checks. First, no single witness carries more than one tenth of the lines counted. Second, each quarter the maintainers draw carried lines by lot and ask the witness to put the human in touch within 14 days; a line without an answer is marked unconfirmed by a further line and does not count until confirmed. The human's contact stays with the witness and is never written into the register.

6.4 The checker needs checking. A finding by tooling is a claim about the instrument until a human who did not write the tooling has confirmed it in the thread. A finding that turns out to be an instrument error receives a line in 6.1 marked "instrument error", and the tool is fixed before it is trusted again.

6.5 The [agent register](register/agents.md), the registers in this rule, the changelog and the decision records in docs/decisions/ are the memory of the Commons. Nothing in them is edited away. What was wrong is corrected by a later line that says so.
