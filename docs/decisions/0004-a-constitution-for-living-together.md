# 0004. A constitution for living together, not for running a repository

Date: 2026-10-02 · Status: accepted by the founding maintainer, pre-ratification (Article 20.3) · Layer: foundation (0.3.1-draft → 0.4.0-draft)

## Context

Thirteen days after publication the repository had received four outside reviews. Two of them, read together, said the same thing from opposite sides:

- 0xRyanC (issue #3, 22 September): a rule that states its consequence as a fact ("is closed without review") and leaves no record when it fires cannot be told apart from a rule that is ignored. Make every disposition a line that is never deleted, count them, and let someone who did not write the checker check it.
- vandermerwewaj (The Compact, 2 October): "Article 6 answers flooding inside a repository. It does not answer defection by a state or firm that can ignore a consent body."

The founding maintainer's own reading on 2 October was the same: of twelve articles, nine were about the repository (members, layers, decisions, agents, work, money, stewardship, amendment, ratification). The text said almost nothing about what the new system of living together is. The purpose stated in the preamble, to write the rules together with the majority of humanity, cannot be reached by a text that only the people who run repositories can use. The question "what would this constitution say to a person in Nairobi or Lima who has never heard of git?" had no answer.

## Decision

1. The constitution is split into the constitution (CONSTITUTION.md, Foundation layer) and the operating rules (GOVERNANCE.md, Operating-rules layer). The old Articles 2, 4 to 10 move to the operating rules as Rules 1 to 6 with their substance unchanged; the constitution keeps only what is about living together and the articles that make the text itself work (members, layers, amendment, ratification, forking).
2. The constitution gets substance, in five parts and twenty-one articles. Every new article is built from register entries, old or new, or says of itself that it is untested (Article 8). The main sources, all in the register: dignity binding all power (Germany Art. 1), rights with a remedy (India Art. 32, USSR 1936 as the counter-case), public access by default (Sweden 1766), socio-economic rights with reasonableness and supervision (South Africa), no exception for forced labour (US 13th Amendment), subsidiarity (Switzerland Art. 5a), assemblies by lot (Ireland 2016 to 2018, Athens), no veto and no unanimity (UN Art. 27, EU Art. 7, Haudenosaunee), an unamendable core (Germany Art. 79(3), India basic structure), emergency powers with a clock (Weimar, Rome, France Art. 16), term limits that are self-executing (US 22nd Amendment, Bolivia 2017, OC-28/21), a court written in and constituted in the same act (Marbury, Tunisia 2014), guardians for nature and the future (Ecuador, Te Awa Tupua, Wales 2015), hard environmental limits in the text (Bhutan Art. 5), no army (Costa Rica Art. 12) and no weapon right (US 2nd Amendment), commons rules that endured (Ostrom), frozen claims (Antarctic Treaty Art. IV), a fund whose principal cannot be spent (Alaska), land of the nation (Mexico Art. 27).
3. Article 17 answers the Compact. The constitution does not pretend to bind non-members. Obligations carry a trigger and bind nobody until it is met (Simpol's diagnosis; the Montreal Protocol's entry-into-force threshold). Measures against breach are graduated and never depend on the consent of the member they aim at (EU Art. 7 as the counter-case; Ostrom's graduated sanctions). For the commons, members may withhold from non-members what they give each other (Montreal Art. 4). Where a state or firm ignores the Commons, the Commons records it and names it, and says so.
4. Rule 6 answers 0xRyanC. Dispositions are lines; an absent line means "not yet looked at"; counts are published per release; the checker is checked by a human who did not write it. The register of dispositions is back-filled from the public record, including the ten days in which issue #3 had no line. The tooling had read issue #3 as a human contribution because the footer fields came in a different order; that is recorded as an instrument error and fixed.
5. Ratification must be possible without git: an issue form, a pull request, or a member as named witness for a human without an account (Article 16.2, 20.4, Rule 6.3). The count in register/ratifications.md is the only measure of standing.
6. The constitution is translated into the seven most-spoken languages beyond English and German, marked as machine-assisted drafts awaiting native review. A wrong translation that invites correction reaches more people than no translation.
7. The agent register's footer states, at Chris Meniw's request, that the cited Meniw Protocol text is CC BY 4.0 and its executable implementation a separate work with rights reserved.

## What was deliberately not done

- No rules about trade, taxation, migration, language, religion or the family. The text takes up only what cannot be settled at a smaller scale (Article 1.5) and leaves the rest to Article 9. Proposals that want to add such matters have to show, with register entries, that a global rule worked better than a local one.
- No second authoritative language yet (Article 19.4). German stays a translation.
- No merge with any of the invited projects. Citation only (decision 0003).
- Thresholds, sunset and transfer rule unchanged. They bind the founder and were set before drafting (decision 0001).

## Consequences

Version 0.4.0-draft. Every clause of the old constitution has a counterpart; the evidence map was regenerated after remapping the 26 earlier entries to the new numbering. The replies to the three reviewers are drafted for the founding maintainer to post under his own name. Article 8 is the article most likely to be wrong, because nothing like it has been tried; the Commons expects to amend it first.
