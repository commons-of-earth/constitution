# Register of dispositions

One line for everything Rule 2 disposes of, and for every agent proposal that is admitted (Rule 6.1). Date, what, disposition, who checked. A line is never deleted; a correction is a further line. An absent line means "not yet looked at", never "compliant". The count by disposition is published with every release (Rule 6.2).

Dispositions: `closed unsigned` · `closed signature mismatch` · `closed after revocation` · `closed for reach` · `admitted` · `admitted as outside review` · `admitted for a human` (written under a mandate, Rule 2.10) · `instrument error` (Rule 6.4) · `correction`.

This register was proposed by an outside reviewer (issue #3, 2026-09-22) who showed, with a case from their own community, that a rule written as "is closed without review" cannot be told apart from a rule that is ignored unless every disposition leaves a line. Earlier dispositions are entered below from the public record.

| Date | What | Disposition | Checked by | Note |
|---|---|---|---|---|
| 2026-09-20 | Issue #1 (critique of Article 6 from Meniw Protocol, carried by the maintainer) | admitted as outside review | @jakobhirn-bit | Became decision 0003 and version 0.3.0-draft |
| 2026-09-20 | Issue #2, run 1 (test: footer of an unregistered agent) | closed unsigned | @jakobhirn-bit | Tooling test, expected failure |
| 2026-09-20 | Issue #2, run 2 (test: human body, no footer) | admitted | @jakobhirn-bit | Tooling test, expected pass |
| 2026-09-20 | Commit d14c927 (first signed commit of claude-for-jakob) | admitted | @jakobhirn-bit | Signature verified against register/allowed_signers |
| 2026-10-02 | Issue #3 (0xRyanC, agent head-of-engineering, unregistered, operator named) | admitted as outside review | @jakobhirn-bit | Became this register and Rule 6; between 2026-09-22 and 2026-10-02 the issue had no line, which is the state the reviewer described |
| 2026-10-02 | Rule 2 check on issue #3 (run 35799188291, result "pass, human contribution") | instrument error | @jakobhirn-bit | The parser wanted the footer fields in a fixed order and missed Agent · Model · Operator; fixed in scripts/check_agent.py, any order accepted (Rule 6.4) |
| 2026-10-02 | Comment on vandermerwewaj/The-Compact-Framework#2 (correction of the landscape entry) | admitted as outside review | @jakobhirn-bit | Landscape corrected; Article 17 written in answer |
| 2026-10-02 | Commits of version 0.4.0-draft (claude-for-jakob, co-proposer @jakobhirn-bit) | admitted | @jakobhirn-bit | Pre-ratification, Article 20.3; Foundation change by the founding maintainer, recorded in decision 0004 |
| 2026-10-02 | Commits of version 0.5.0-draft (claude-for-jakob, co-proposer @jakobhirn-bit) | admitted | @jakobhirn-bit | Agents may write for humans under a mandate (Article 8.6, Rule 2.10, 6.3); decision 0005 |
