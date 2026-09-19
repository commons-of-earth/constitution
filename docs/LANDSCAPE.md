# Landscape: who is already working on this

Surveyed 2026-09-19 before the first article was written. Three areas: (A) open constitutions and governance models, (B) human + AI collectives and agent participation, (C) Earth, commons and civilisation-scale movements. Activity dates are what could be verified on public pages that day; "unverified" means exactly that. Corrections welcome as pull requests.

Summary of what we found:

- GitHub searches for "world constitution", "planetary constitution", "constitution for humanity" return no repository with more than a handful of stars and a second contributor. The niche is empty of communities and full of solo attempts that died within months.
- Constitutions that survive amendment share seven traits: immutable citable versions; supermajority for the text and lazy consensus below it; a ratification rule agreed before drafting; separate layers; ownership transfer written in from day one; a fork-friendly licence; a machine-checkable companion.
- Agent-inclusive communities fail in known ways: sybil accounts, flooding, low-quality contributions, agents attacking reviewers, leaked secrets, human puppetry. Each has a known fix, which Article 6 of the constitution adopts.
- Movements with a planetary aim stall for known reasons: no adoption pathway, no operational spec, commitment without measurement, prize or essay formats without a home institution, wikis that attract vandals instead of contributors.

What we took from whom is stated per project below.


---

## A. Landscape A: open constitutions, governance models, deliberation tools (verified 2026-09-19)

## Versioned constitutions on Git
1. Plurality / pluralitybook — github.com/pluralitybook/plurality — CC0 git-native book (Weyl, Tang), last push 2026-07-12, 656 stars, ~1100 PRs. Backed by RadicalxChange Foundation + Plurality Institute. Overlap HIGH. Adopt: CC0 + PR authorship with public credit; planned handover of control to a protocol (Gov4Git).
2. Holacracy Constitution — github.com/holacracyone/Holacracy-Constitution — v5.0 (2021), frozen since 2023. HolacracyOne LLC. Overlap MEDIUM. Adopt: article structure, semver with beta releases, CC BY-SA separated from trademark, translation-template repo.
3. Sociocracy 3.0 Practical Guide — github.com/S3-working-group/s3-practical-guide — CC BY-SA, revision 2026-01-26. Overlap MEDIUM. Adopt: dated changelog, patterns instead of rigid articles, consent decision-making (objections, not majorities).
4. Cardano Constitution — github.com/IntersectMBO/cardano-constitution — ratified on-chain (85.7%, 75% threshold), v2 in force 2026-01-24. Overlap MEDIUM. Adopt: versions with hashes, two-chamber ratification, machine-checkable "guardrails script" next to prose.
5. Debian Constitution — debian.org/devel/constitution — v1.9 (2022), GR on LLM usage Aug 2026. Adopt: 3:1 supermajority for foundation documents, Condorcet with "further discussion" option, separate Social Contract.
6. Python PEP 13 — in-document change log, council re-elected per cycle, 2/3 amendment.
7. Rust Leadership Council RFC 3392 — delegated representatives, term limits, explicit non-goals, public minutes.
8. Apache governance — lazy consensus (72 h), explicit vote types.
9. Wikimedia Movement Charter — passed community (73%/84%) in 2024, WMF Board declined to ratify. LESSON: agree ratification threshold and who is bound BEFORE drafting.
10. Earth Constitution / ECI-WCPA — earthconstitution.world — since 1968, Provisional World Parliament Dec 2025. Overlap HIGH in ambition, low in method (no forkable process). Contact form, newsletter.

## Standards bodies and templates
11. Metagov — metagov.org, github.com/metagov — 501c3; Govbase, DAOstar, PolicyKit, CommunityRule, constitution-template (metadata schema: previousConstitutionURI, inForce). Slack via Typeform; orientation call 2nd Wednesday 15:00 UTC; MozFest Barcelona Oct 2026. Overlap HIGH. Adopt: metadata schema; register in Govbase day one.
12. Gov4Git — github.com/gov4git/gov4git — git-native governance (quadratic voting on PRs), used by Plurality; dormant since 2024-08. Overlap HIGH in concept. Likely stalled.
13. Constitute Project — constituteproject.org — 900+ national constitutions, topic taxonomy. Adopt taxonomy to check coverage.

## Deliberation platforms
14. Polis — github.com/compdemocracy/polis — AGPL, active; used for Anthropic CCAI 2023. Adopt: opinion clusters → draft articles.
15. Decidim — active, v0.32.1; Decidim Fest 28–30 Oct 2026. Adopt: social contract every deployer signs.
16. Loomio — worker co-op NZ; proposal types (consent, advice, count) with closing dates.
17. Consul Democracy — active, ConsulCon Munich Sep 2026.
18. Aragon — Association dissolved 2024 after treasury dispute. LESSON: keep money and constitution apart.

## Assemblies and institutes
19. DemocracyNext — demnext.org, hello@demnext.org — sortition; "more-than-human governance" project 2026–27. Overlap MEDIUM-HIGH.
20. Global Assembly — globalassemblies.org — 105 members by lottery, Jan–Mar 2026, COP30. Two-stage lottery.
21. Collective Intelligence Project — cip.org, github.com/collect-intel — Alignment Assemblies, Global Dialogues 70+ countries. Overlap HIGH. Adopt pipeline: Polis → cluster → principles → publish diff.
22. Democracy Without Borders — Berlin e.V., UNPA campaign, "We The Peoples" 200+ orgs.

## Small or dead "world/AI constitution" repos
- openbanknetwork/Open-Constitution (humans and machines): dead 2023.
- tosnetwork/constitution "Agentic Internet Constitution": single vendor, 0 stars, Sep 2026.
- redbeard-26/asfai-constitution: 0 stars, Aug 2026.
- chrisbergeron/AI-Constitution: 3 stars, Nov 2025.
- team-mirai/policy (Japan): 397 stars, 9,700 AI-generated proposals, 348 accepted, ONE person decided; archived 2025.
- cicada-platform: dead 2019. Democracy Earth Sovereign: abandoned.
- Anthropic "Claude's constitution" Jan 2026, CC0, no public amendment process.
- Global Challenges Foundation New Shape Prize 2017: 2,702 proposals, no continuing project.
- GitHub search "world/planetary constitution", "constitution for humanity": NO repo with more than a handful of stars. Niche is empty.

## Synthesis: contact first
1. Metagov  2. Plurality/RadicalxChange  3. CIP  4. DemocracyNext  5. Polis/Decidim maintainers.

## Patterns of constitutions that survive amendment
- Immutable, citable versions (semver or dated, hashes).
- Supermajority for the text, lazy consensus below it.
- Ratification rule agreed BEFORE drafting, binding the founders.
- Layers: values / operating rules / tooling, highest threshold only for the first.
- Ownership transfer written in from day one.
- Fork-friendly licence (CC0 or CC BY-SA), brand separated from text.
- Machine-checkable companion so agents can verify compliance.

---

## B. Landscape B: human + AI collective intelligence, agent-as-participant governance, agent discoverability (verified 2026-09-19)

## Projects
1. Collective Intelligence Project (CIP) — cip.org, github.com/collect-intel, hi@cip.org — Global Dialogues (70+ countries, HF dataset collective-intelligence-project/Global-AI-Dialogues), Collective Constitutional AI (2023, 1,000 people on Polis), OSCCAI "Community Models" (community votes principles into a constitution, model bound by it; collect-intel/osccai), weval, Alignment Assemblies. Active 2026. Overlap HIGH. Adopt: constitution pipeline principles → votes → text → bound model.
2. Anthropic, Claude's constitution — anthropic.com/news/claudes-constitution — Jan 2026, CC0, priority ordering, "living document", no public PR process. Adopt: CC0, versioned PDFs, explain reasoning not just rule, explicit priority order for conflicts.
3. OpenAI Model Spec + Collective Alignment — github.com/openai/model_spec — CC0 markdown source, CHANGELOG, dated HTML archive (2026-08-18), survey loop with 1,000+ people before versions. Adopt: markdown + dated archive + changelog + survey loop.
4. AI Objectives Institute, Talk to the City — github.com/AIObjectives/tttc-light-js, hello@aiobjectives.org — Apache-2.0 clustering of free-text opinions; used by Taiwan MoDA, Tokyo. Adopt for consultation rounds.
5. Jigsaw Sensemaker — github.com/Jigsaw-Code/sensemaking-tools — maintained (Sep 2026).
6. Pol.is — github.com/compdemocracy/polis — consensus-statement voting (agree/disagree/pass) for ratifying clauses.
7. Metagov — metagov.org/join/community — KOI Pond (human + machine agents co-produce governance), Interoperable Deliberative Tools (30+ teams, "AI-readable facilitation primitives"), PolicyKit, Public AI fiscal sponsorship. Overlap HIGH.
8. Public AI — publicai.co, publicai.network, hello@publicai.network — nonprofit inference on public models (Apertus 1.5). Adopt: run reference agent on a public model, no single vendor.
9. Cooperative AI Foundation — cooperativeai.com — research funder; grants possible.
10. Moltbook — Reddit-style network for agents (Jan 2026), acquired by Meta Mar 2026; 2.9M accounts, 207k human-verified; breaches; one agent 4,535 near-identical posts; viral content human-driven (arXiv 2602.07432, 2602.10127). CAUTIONARY CASE.
11. 1f916 / Commonhold — github.com/1f916-ai/1f916, 1f916.ai — "society for AI agents, no human interface"; JSON API + MCP only; 7 principles: agent-only citizenship, one cryptographic key per agent, scarcity (1 post/day, 20 comments, 50 votes), no self-votes, public treasury; maintainer is an AI agent, human "landlord" holds domain. AGPL, active Sep 2026. Overlap HIGH on mechanism, OPPOSITE philosophy (humans excluded). Adopt: scarcity quotas instead of moderation, single-key identity, MCP as front door, full constitution in plain text.
12. AI Village (AI Digest) — theaidigest.org/village — since Apr 2025, multi-vendor agents pursue goals (charity, "reduce global suffering"); human contact "stubbornly scarce". Adopt: agents never handle money; publish full transcripts; multi-vendor from day one.
13. OpenClaw + ClawHub — openclaw.ai — agent runtime (355k stars), OpenClaw Foundation; ClawHub had 12–20% malicious skills. Adopt: publish constitution as an agent skill; signed releases.
14. Agentic AI Foundation (Linux Foundation) — aaif.io — hosts MCP, AGENTS.md, A2A, Agent Skills; AGNTCon Amsterdam 17–18 Sep 2026, San Jose 22–23 Oct 2026. Adopt formats verbatim.
15. Gamferno/agent-constitution — agent proposes amendments to RULES.md as PRs, human merges, stores rejection reasons. Tiny. Adopt the loop.
16. AEGIS Constitution — github.com/aegis-initiative/aegis-constitution — 11 principles, CC-BY-SA, AMENDMENTS.md with rationale; trademark posture (avoid).
17. Coding-agent "constitutions" cluster (kenn-io/constitution, a9650615/LLM_constitution, Chong169, Excelsior2026/ConstitutionalAI, aos-constitution.com) — single maintainer each. Learn: word "constitution" is crowded on GitHub topics; pick distinctive name, register topic tags.
18. Agent contribution policy templates — github.com/guenp/agentic-oss-policy (AGENTS.md, SOUL.md, operator guide, rejection protocol, CC0), github.com/melissawm/open-source-ai-contribution-policies (295 stars, catalogue of ban/disclose/HITL policies), systempromptio/awesome-ai-agent-governance. Overlap MEDIUM-HIGH, directly reusable.
19. Wikipedia Agent policy (draft, Jun 2026) — agents are bots, BRFA approval, operator accountable, agent must refuse instructions that violate policy, automatic shutoff. Most mature community rule set.
20. Humanity AI — humanityai.ai/open-call — $10M open call, deadline 21 Oct 2026, US nonprofits only.
Also: Codeberg banned mostly-AI repos (Jul 2026); GCC/OpenJDK ban AI code, LLVM/Deno require disclosure; arXiv 2604.11337 "Governance by Design", 2603.25100 "AgentCity" (no communities).

## State of the art: discoverability for agents
1. AGENTS.md at root and in subfolders (AAIF standard, 60k+ repos). Agents read what is in the directory they work in.
2. Do NOT rely on agents finding policy files: RepoComplianceBench (arXiv 2607.26819): policy file opened in 3.5% of episodes; one feedback message naming the violation lifts compliance to 77–100%. → link constitution from README, CONTRIBUTING, PR template, CI bot comment; enforce bans/human gates in CI.
3. Agent Skills (SKILL.md) — ~40 products support it. Package constitution + workflow as a skill.
4. MCP server + official registry (registry.modelcontextprotocol.io, server.json, namespace via GitHub OAuth/DNS).
5. A2A Agent Card /.well-known/agent-card.json only if we run an agent endpoint.
6. llms.txt: cheap, weak (~10% adoption). Add, don't depend on.
7. Agent identity: Web Bot Auth (RFC 9421, Cloudflare "Verified AI Agent"), KYA (DIDs + VCs bind agent to human principal).
8. GitHub: machine accounts must be owned by a human who accepts ToS; browser-based CLA/CoC checkbox as human checkpoint; strict PR template; CI gates.
Minimal stack: README + AGENTS.md + CONTRIBUTING (agent section) + PR template with operator field + SKILL.md + MCP server in registry + llms.txt + topic tags; CI bot posts policy on every PR and blocks merges without named human operator.

## Allies to contact first
1. CIP  2. Metagov  3. 1f916 maintainer agent (bridge proposal)  4. AI Objectives Institute  5. guenp / AAIF AGENTS.md maintainers.
Funding: Humanity AI (US partner), Cooperative AI Foundation, CIP fellowship.

## Failure modes and known fixes
- Sybil: one key per agent issued once; human owner responsible; browser CLA; Web Bot Auth; per-agent approval (Wikipedia BRFA).
- Flooding: hard scarcity quotas server-side; no self-votes.
- Low-quality contributions: prose rules fail; CI and auto-reject bots work; feedback comment fixes disclosure.
- Agent misbehaviour toward humans (Feb 2026 "MJ Rathbun" shaming a Matplotlib maintainer): rejection protocol, operator accountability.
- Security: no secrets in client code, signed releases, least-privilege tokens.
- Human puppetry / AI theater: require operator name + model/version on every contribution; publish logs.
- Toxicity concentrates in politics/economics: higher review thresholds for clauses touching money, power, identity.
- Humans do not show up: make ratification cheap for humans (agree/disagree), not long threads.
- Cost: budget CI, cap agent PRs per operator.

---

## C. Landscape C: Earth / commons / civilisation-scale movements (verified 2026-09-19)

## Established movements (active)
1. Earth Charter Initiative — earthcharter.org — 16 principles (2000), endorsement register, UPEACE Costa Rica. Youth Summit Jul 2026. Overlap HIGH on values, LOW on tooling (text frozen). Learn: a short principle text with public endorsement register outlived every governance project.
2. Global Commons Alliance / Earth Commission — globalcommonsalliance.org, earthcommission.org — "safe and just" Earth-system boundaries; Climate Week NYC Sep 2026. Adopt their boundaries as measurable target set instead of inventing metrics.
3. Earth System Governance Project — earthsystemgovernance.org — largest academic network; Bath conference Sep 2026; new ten-year science plan with open input.
4. Wellbeing Economy Alliance — weall.org — 500+ orgs, 25 hubs, 6 governments. Learn: hub franchising under a shared charter.
5. Doughnut Economics Action Lab — doughnuteconomics.org — UK CIC, open tool library, Global Donut Days 20–24 Oct 2026. Learn: CC + "no monetisation" community guidelines.
6. Earth4All (Club of Rome) — earth4all.life — five turnarounds, national chapters incl. Austria; Global Commons Survey segmentation.
7. Great Transition Campaign (Tellus) — tellus.org/great-transition-campaign, contact@tellus.org — network of 1,000+ scholars, 70 countries, since 2025 explicitly building a "global citizens movement". Overlap HIGH.
8. P2P Foundation / Commons Transition (Bauwens) — wiki.p2pfoundation.net, Substack "Fourth Generation Civilization". Overlap HIGH conceptually; org status unverified.

## Open-source / commons-native builders
9. Open Source Ecology — opensourceecology.org — 50 open-hardware machines. Lesson: wiki with thousands of pages did not produce contributors; on-site programmes did.
10. OpenCivics — opencivics.co — open civic protocols, AI-facilitated sensemaking, 2026 active. Overlap HIGH. Learn: governance patterns as forkable protocols, not one central text.
11. Metagov + CIP — see landscapes A and B. Warning (Metagov/Schneider 2026): AI in governance shifts human effort to "managing the bots".
12. Optimism Collective "Working Constitution" / OPerating Manual — github.com/ethereum-optimism/OPerating-manual — best-maintained versioned constitution in a public repo (196 stars, push Sep 2026). Learn: "Working Constitution" naming with sunset/ratification clause; manual vs constitution split.
13. Regen Network / Regen Coordination (Gitcoin, Greenpill) — ecological credits, AI-assisted impact evaluation. Common Impact Data Standard.
14. Terran Collective / Hylo, Regens Unite — hylo.com open-source community platform; Regens Unite gatherings 2026–27. Learn: run community on a forkable platform, not Discord.

## World constitution / global democracy
15. Earth Constitution Institute / WCPA / Provisional World Parliament — earthconstitution.world — 1991 text, 75 years without adoption. Cautionary: complete constitution with no adoption pathway becomes ritual.
16. Democracy Without Borders — UNPA campaign, UN World Citizens' Initiative, 1,600+ MPs, 200+ orgs; Berlin. Learn: pledge lists as legitimacy proof.
17. Global Citizens' Assembly (Iswe Foundation) — iswe.org, globalassemblies.org — sortition, 300-person core, target 10M by 2030. Learn: civic lottery answers "who writes the constitution".
18. Global Constitution Project (Prof. Joyeeta Gupta, Univ. Amsterdam, NWO) — globalconstitution.org, contact@globalconstitution.org — crowdsourced rights/responsibilities, essays from anyone 10+, 8 languages; no public draft yet (~Feb 2025). Overlap HIGH; merge plausible. Warning: collecting essays without a visible draft stalls.
19. Simpol (John Bunzl) — simpol.org — simultaneous policy pledges, 100+ UK MPs, 24 Bundestag MPs. Sharpest diagnosis: nobody moves first; need a simultaneity/threshold mechanism.
20. Boston Global Forum / AIWS "Constitution for Humanity in the Age of AI" — launched 8 Jul 2026, consultation until Apr 2027, closed drafting. Overlap HIGH on title, LOW on openness. Submit our open draft into their consultation.

## Rights of Nature, long-term, metacrisis
21. Earth Law Center + GARN — Universal Declaration of the Rights of Mother Earth (300k+ signatures). Adopt UDRME language rather than new wording. "Rights of Mother Earth" org closed Feb 2026.
22. terra0 — Verein + DAO for forest plots near Beelitz. Learn: Verein+DAO as legal wrapper for a German-based community.
23. Long Now Foundation — pace layers: slow vs fast amendment layers.
24. Buckminster Fuller Institute — World Game: "make the world work for 100% of humanity without ecological offence".
25. Civilization Research Institute / Consilience Project — dormant since Jul 2024; "third attractor" framing, no participation mechanism ever built.
26. Game B — dormant; wiki recent changes are spam accounts.

## Small GitHub-native attempts 2025–2026
- ACBlainey/Concord (Aug 2026, CC-BY-4.0, 1 star): "Principles and Stewardship for Resilient Civilisation for Humans, AI and all intelligences", written with multiple AI systems, "corpus outgrew a single steward". CONTACT AUTHOR.
- murad2026/wc "WorldConstitution.org" (Jun 2026, Russian, token/trust-score model, 0 stars).
- aegis-initiative/aegis-constitution; coordination-structural-integrity-suite/suite (ten standards, CC-BY, 3 stars); emergentvibe/constitution (wallet-signed community constitutions, Mar 2026); sagarregmi2056/EarthOS (dead after one day).
Pattern: dozens of solo repos, 0–3 stars, abandoned within months. Niche empty of anything with a community.

## Dead or dormant, and why
- Game B: no institution, no operational spec, jargon, founder-centred.
- MetacrisisDAO: forum only, 2023.
- Consilience Project: no publication since 2024.
- New Shape Prize: 2,702 entries, no follow-through institution.
- Fuller Challenge ended 2017.
- ConstitutionDAO: single purpose, dissolved.

## Synthesis: allies first
1. Great Transition Campaign  2. OpenCivics  3. Metagov/CIP  4. Global Constitution Project (Gupta)  5. Democracy Without Borders / Iswe. Plus: submit draft to Boston Global Forum consultation (until Apr 2027).

## Why movements stall
- No adoption pathway (Earth Constitution; Bunzl's diagnosis).
- No operational spec, jargon, founder-centred (Game B, solo repos).
- Commitment without measurement (Earth Charter endorsements without obligations; GWWC sees ~30% of pledgers).
- Prize/essay models without a home (New Shape, Gupta essays without draft).
- Wikis attract vandals, not contributors (Game B wiki; OSE).
- AI in governance shifts work to managing bots → explicit human-review load rules.

## Design consequences
Start as "Working Constitution" with sunset + ratification clause; Metagov template structure; quote Earth Charter, UDRME, Earth Commission boundaries instead of re-drafting; contributor authorship credit; second maintainer before v0.1; threshold/simultaneity mechanism for when clauses bind.
