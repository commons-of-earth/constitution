## Layer touched
<!-- one of: foundation (CONSTITUTION.md) / operating rules (GOVERNANCE.md) / tooling / register / translation / ratification -->

## What changes

## Why (with sources, Article 5.1)

## Author
- [ ] I am a human and I accept the constitution (CONSTITUTION.md, current version)
- [ ] This was written by an agent. Footer below is complete (agent, operator, model, key fingerprint), the key is in register/agents.md and the commits are signed with it (Rule 2.2)
- [ ] If an agent touches CONSTITUTION.md, GOVERNANCE.md, de/VERFASSUNG.md, de/REGELN.md or constitution.json: a human member is named as co-proposer (Rule 2.4)
- [ ] If this adds a ratification line: I am the human on the line, or I am named as witness and answer for it (Rule 6.3)

<!-- Co-proposer: @handle -->
<!-- Agent: … · Operator: … · Model: … · Key: SHA256:… -->

The Rule 2 check (.github/workflows/agent-check.yml) runs scripts/check_agent.py on every pull request and issue and writes its findings into the log. A finding is a claim about the instrument until a human who did not write the tool confirms it (Rule 6.4). Every disposition gets a line in register/dispositions.md (Rule 6.1).
