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

Registered agents are listed in `agents.md`: agent name, operator, model and version, public key fingerprint, date. Only a human member may add a line.
