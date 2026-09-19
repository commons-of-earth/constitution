# Register of problems

The working memory of the Assembly (Article 7). One file per entry in `entries/`, validated against `schema.json`.

An entry is accepted when it has a source for the current state and a target that a stranger could check. Opinion without evidence is closed.

## Fields

| Field | Meaning |
|---|---|
| id | short slug, stable forever |
| title | one line |
| place | country, region or "global" |
| field | e.g. built-environment, energy, water, food, governance |
| current_state | number or fact with source and date |
| target | number or fact, with date by which it should hold |
| boundary | which Earth Commission boundary or other adopted limit this serves |
| evidence | list of sources |
| status | proposed / accepted / in-progress / verified / closed |
| people | human members working on it |
| agents | registered agents working on it |
| commitment | optional, per Article 11.4: text of the commitment and the number of signatories needed before it binds |

## Agents

Registered agents are listed in `agents.md`: agent name, operator, model and version, public key fingerprint, date. Only a human member may add a line.
