# Prompt test report: gym game app

Date: 23 October 2026. Prompt tested: `prompt-v1.md`. Idea: a gym game that keeps people consistent, with ranks and stats for lifting, fitness and size. Full output: `plan.md`. Arithmetic: `money.py`.

**Verdict:** the prompt works. It produced all 13 sections and the checklist, forced real citations, and its compliance rule changed the plan in a useful way. It has 10 gaps, all fixed in `prompt-v2.md`.

## Tests run

| # | Test | What happened | Result |
|---|---|---|---|
| 1 | Idea only, no city, budget or deadline | Asked 4 questions in one batch of multiple-choice pop-ups, recommended option first | Pass |
| 2 | Answer "all of the above" to payer and city | The prompt has no rule for this. I had to invent the choice (one SA city first, London later). Without the "recommend one option" rule it could have planned for 4 cities at once | Partial |
| 3 | All 13 sections plus checklist | All present | Pass |
| 4 | No invented facts | Every figure is cited and dated, or labelled unverified or secondary. Two things had no reliable source: number of gyms in SA (estimates of 1,100 and 3,500 conflict) and Cape Town box prices | Pass, but the prompt should say what to do when no reliable figure exists |
| 5 | Compliance check before outreach | Found that POPIA treats companies as data subjects and allows one consent request only, so cold WhatsApp in SA is out and walk-ins come first. UK: cold email to limited companies is fine, sole traders need consent | Pass, and it changed the plan |
| 6 | Arithmetic in code | `money.py` ran; it showed fixed costs of £75 a month, over the £50 budget. The plan then gave a £16 version | Pass, but the prompt did not ask for a budget check, so it relied on judgement |
| 7 | Ask before publishing or messaging | All 5 outgoing drafts marked APPROVAL; nothing sent | Pass |
| 8 | Public business details only | Owners' names were public on CrossFit.com; I left them out, but the prompt does not say whether names of people count | Partial |
| 9 | Data rules for the app itself | The prompt only asks about outreach rules. Body measurements are likely health data, which has stricter rules. I caught it under Risks, but the prompt did not ask | Partial |
| 10 | "First 10 clients" in 4 weeks with a 6-week pilot | These conflict: nobody can pay before week 7. I redefined it as 10 gyms on a free tool or pilot | Fail (prompt contradiction) |
| 11 | Follow-up answers: Josh in Gqeberha, Cam in Aberdeen, not registered, demo exists | The prompt assumed both partners share one "area". The answers changed the cities, prospect list, channels, laws, payment providers, pilot dates and money split. v1 has no instruction to redo affected sections, so it depended on judgement | Partial |
| 12 | Seasons | Not in v1. A 6-week SA pilot from November would run into the December holidays and measure people going away. Caught only because the plan worked out real dates | Partial |

## Gaps found and the fix in v2

1. **"All of the above" answers:** v2 says to pick one, say why, and say when the others come in.
2. **Missing questions:** v1 never asks where your business is registered (this decides payment provider and tax) or what exists today (idea, demo or app). v2 adds both.
3. **First 10 clients versus pilot length:** v2 defines "first 10" as on a free tool or pilot by week 4, and asks when the first one pays.
4. **No reliable figure:** v2 says to show the conflicting estimates instead of picking one, and to label vendor blogs as secondary.
5. **Budget check:** v2 says to flag any cost over budget and give the cheapest version under it, and to show costs before and after the first paying client.
6. **Data the users put in:** v2 adds health data, children's data and a data agreement with the client to the rules check.
7. **People's names:** v2 says no individuals' names or personal contact details.
8. **Partners in different countries:** v2 asks where each partner lives and splits the 4-week plan by city.
9. **Answers that change earlier assumptions:** v2 says to redo every section they affect.
10. **Real dates and seasons:** v2 asks for real dates in the 4-week plan and a flag for holidays that would distort a pilot.

Smaller changes in v2: a 5-line summary at the top (v1 says "lead with the answer" but 13 long sections bury it), state the exchange rate and its date, name verified competitors in section 4, show our hours per month in section 10, and "(B2B ideas only)" reworded to "(only if the client is a business)".

## Worth knowing

- The two rounds used about 45 web searches. On a tight usage budget, expect each full run to be heavy. If that matters, run sections 1 to 4 first, then 5 to 13 in a second message.
- After the follow-up answers, drafts only keep per-gym blanks such as `[gym name]`, which is right for messages sent to many gyms.
- Biggest business finding from the second round: Gqeberha has only 2 CrossFit affiliates listed, while Aberdeen gyms charge around £99 a month, so Aberdeen is the stronger first market.
