# Gym game app: customer-base plan (prompt test run)

Test run of `prompt-v1.md` on the gym game idea, 23 October 2026, updated with your answers: Josh is in Gqeberha (Port Elizabeth), Cam is in Aberdeen, Scotland; studio name "Josh and Cam" for now; business not registered; a demo or mock-up already exists; budget up to £50 a month; first paying gym within 3 months (by 23 January 2027).

**The answer:** each of you sells in your own city. Josh walks into Gqeberha boxes and gyms; Cam walks into Aberdeen ones. Offer a free monthly leaderboard for the gym TV, turn it into a free 6-week pilot with a written pass mark, then charge £55 (R1,200) a month in SA and £79 a month in Aberdeen. Members use it free. Rank members mainly on consistency and personal improvement, not raw weight. Build it as a web app, not an App Store app. Aberdeen is the stronger market: more gyms, higher prices (CrossFit Aberdeen charges £99 a month for strength-area-only access), and no December summer holiday to wreck a pilot. On these numbers, 20 paying gyms leaves about £706 (R15,329) a month each, before tax. New spend before the first paying gym is about £20 (R443) a month.

**Assumptions and recommendations (change any of them):**
- **Who pays:** gyms pay, members use it free. Personal trainers come later as a cheaper tier; direct-to-member sales and big chains are parked. Reason: one gym signing gets you 50 to 200 users at once, the owner feels the cost of members leaving, and you need no ad budget.
- **Cities:** Gqeberha and Aberdeen only, because in-person visits are your best channel and the SA rules make cold messages hard. Johannesburg, Cape Town, Pretoria and London from the first test run are parked until each city has 2 case studies.
- **Money between you:** I recommend each of you keeps what your own country's gyms pay, and you split shared costs 50/50. That avoids sending money across borders every month. At a 50/50 client mix it comes to the same as an equal split. This is your call.
- **Exchange rate:** £1 = R21.72 (longforecast.com, 9 September 2026). Not today's rate; re-check before quoting a client.
- **Time zones:** UK clocks go back on 25 October 2026, so Aberdeen is 2 hours behind Gqeberha. Weekly call: Sunday 19:00 Gqeberha, 17:00 Aberdeen.

---

## 1. The client in one line

The gym owner pays; the members use it; today they rely on a whiteboard, an Instagram post or a booking app's attendance list, and nobody notices a member drifting away until they cancel.

## 2. Why they would pay

| Figure | Source | Notes |
|---|---|---|
| Average member retention is 66.4% a year, so about 1 in 3 members leaves each year | [Health & Fitness Association, 2025 benchmarking report](https://www.healthandfitness.org/publications/the-2025-hfa-global-report/) (175 companies, 17,000+ facilities) | Global benchmark, not city-specific |
| CrossFit Aberdeen charges £99 a month for unlimited strength-area-only access | [CrossFit Aberdeen on TeamUp](https://goteamup.com/p/8426-crossfit-aberdeen/memberships/) | Their full membership will cost more; not listed in what I read |
| Kimura CrossFit (Aberdeen) charges £12 for a drop-in class | [kimuracrossfit.com](https://kimuracrossfit.com/) | Monthly prices sent on request |
| CrossFit Valley Road (Gqeberha) charges R150 (£7) for a drop-in class | [crossfitvalleyroad.co.za](https://crossfitvalleyroad.co.za/fitness-events-gqeberha-port-elizabeth/) | Monthly prices sent on request; ask on visits |
| One SA box charges R740 (£34) a month unlimited | [CrossFit Plettenberg Bay booking page](https://cfplett.pike13.com/shop) | Used as the SA example until you get Gqeberha prices |
| Independent single-site UK gyms charge £41.94 a month on average | [LeisureDB 2025, via Health Club Management](https://www.healthclubmanagement.co.uk/health-club-management-news/Industry-metrics-are-at-an-all-time-high-says-LeisureDB-David-Minton/356016) | UK-wide list prices |
| 53% of members say they stopped attending at some point without cancelling | [Zenoti survey](https://www.zenoti.com/es/thecheckin/silent-churn-crisis-2026-gym-membership-data) | Vendor survey, secondary |
| Weekly leaderboards in teams of 3 added 920 steps a day, and were the only game design whose effect lasted after it stopped | [STEP UP randomised trial, JAMA Internal Medicine 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6735420) | Steps, not gym visits, but the best evidence that competition works |

The money problem, calculated in `money.py`: a 100-member SA box at 66.4% retention loses about 34 members a year, worth R298,368 (£13,737) in a year of fees if none are replaced. The gym breaks even on our price if the app keeps:
- **1.6 members** a month who would otherwise leave, in SA (R1,200 against a R740 member)
- **0.8 members** a month in Aberdeen (£79 against a £99 member). In Aberdeen, keeping one member pays for the app.

## 3. Real target list

**How many exist:** CrossFit.com lists only **2** affiliates in Gqeberha, Lions Bay CrossFit and CrossFit Valley Road ([CrossFit.com South Africa directory](https://www.crossfit.com/gyms/south-africa), checked 23 October 2026). For Aberdeen and Aberdeenshire I found 5 boxes across CrossFit.com and directories. I found **no reliable count** of all gyms in either city. Gqeberha is a small box market, so Josh's list includes studios and functional-training gyms, and later the boxes in East London ([CrossFit East London](https://www.crossfit.com/gym/18087/crossfit-east-london)) and Port Alfred ([No Limits CrossFit](https://www.crossfit.com/gym/35525/no-limits-crossfit)).

**First 20 prospects** (public business pages only; owners' names and phone numbers left out on purpose). Several come from directories that may be out of date: confirm each is still trading before visiting.

| # | Name | Area | Public page | Why they fit |
|---|---|---|---|---|
| **Josh: Gqeberha** | | | | |
| 1 | Lions Bay CrossFit | Fairview | [CrossFit.com page](https://www.crossfit.com/gym/17265/lions-bay-crossfit) | Hosted the Fittest in PE competition on 9 to 11 October 2026: a competitive community that will like ranks |
| 2 | CrossFit Valley Road | South End | [crossfitvalleyroad.co.za](https://crossfitvalleyroad.co.za/) | Runs its own website and events guide: already thinks digitally |
| 3 | CrossFit Algoa | Newton Park | [City of Gqeberha listing](https://cityofgqeberha.co.za/tag/crossfit-gyms-in-pe/) | Venue for the East Cape Champs; not on CrossFit.com's list, so confirm it still trades |
| 4 | The Fitness Box with CrossFit | Walmer | [Discovery Vitality gym list (PDF)](https://www.discovery.co.za/wcm/discoverycoza/assets/vitality/vitality-news/vitality-wellness-network-list-affiliated-gyms.pdf) | Box-style gym in a strong suburb; list is about 600 days old |
| 5 | Hybrid Performance Training Club (REBOOTZ) | Walmer | [Fresha Walmer listing](https://www.fresha.com/lp/en/bt/gym-and-fitness/in/za-port-elizabeth/walmer) | Hybrid training club: same crowd as HYROX, likes measurable progress |
| 6 | Tamara's Personal Training Studio | Newton Park | [magicpin page](https://magicpin.com/south-africa/Gqeberha/Walmer/Fitness/Tamaras-Personal-Training-Studio/store/2339383) | Small studio rated 4.8: test the cheaper trainer tier here |
| 7 | Profiles FX | Mount Pleasant | [Discovery Vitality gym list (PDF)](https://cdn.discovery.co.za/wcm/discoverycoza/assets/vitality/vitality-news/vitality-wellness-network-list-affiliated-gyms.pdf) | Vitality partner gym: members already used to earning points for visits |
| 8 | Ignite Fitness Walmer | Walmer | [Directory listing](https://rsa.worldorgs.com/catalog/gqeberha/gym/ignite-fitness-walmer) | Well reviewed; may be part of a group, so ask who decides |
| **Cam: Aberdeen** | | | | |
| 9 | CrossFit Aberdeen | St Clement Street | [CrossFit.com page](https://crossfit.com/gym/1499/crossfit-aberdeen) | North-east Scotland's original box; had an 80-person waiting list at its old venue ([Insider](https://www.insider.co.uk/news/plans-new-aberdeen-crossfit-gym-35706844)) |
| 10 | Results Gym | South College Street | [resultsgym.co.uk](https://resultsgym.co.uk/) | Independent, 3 gyms, 20+ years, powerlifting and strongman: an inter-site league and strength ranks fit |
| 11 | Kimura CrossFit | Cove Bay | [kimuracrossfit.com](https://kimuracrossfit.com/) | Runs HYROX, a 65+ class and youth classes: divisions matter here |
| 12 | Edge Performance Gym | Aberdeen | [edgeperformancegym.co.uk](https://www.edgeperformancegym.co.uk/) | Calls itself a premium HYROX club: premium-tier prospect |
| 13 | CrossFit SAR | Cults | [CrossFit.com page](https://www.crossfit.com/gym/35482/crossfit-sar) | Box in a well-off suburb |
| 14 | CrossFit Shire | Inverurie | [Playsport page](https://playsport.com/crossfitshire_ag_a9543619) | Described as the only box in its area: loyal local members |
| 15 | CrossFit Royal Deeside | Banchory | [CrossFit.com page](https://www.crossfit.com/gym/36533/crossfit-royal-deeside) | Small-town box; pair with SAR for a Deeside league |
| 16 | Bodbox Aberdeen | Scotstown Road | [bodbox-aberdeen.com](https://www.bodbox-aberdeen.com/) | Boxing and fitness, beginners to pros: ranks by experience level |
| 17 | Aberdeen Combat Centre | Aberdeen | [aberdeencombatcentre.com](https://www.aberdeencombatcentre.com/) | Martial arts gyms already use belt ranks; add attendance ranks |
| 18 | Aberdeen Fitness | Aberdeen | [aberdeenfitness.com](https://aberdeenfitness.com/) | Women-only, includes weightlifting; listing about 289 days old |
| 19 | UK Fitness Personal Training | Aberdeen | [ukfitnesspersonaltraining.com](https://www.ukfitnesspersonaltraining.com/) | Independent trainer: test the trainer tier in the UK |
| 20 | Byron Boxing Club | Northfield | [Facebook page](https://www.facebook.com/byronboxingclub/) | Non-profit community club: a free showcase partner and strong case study, not a payer |

## 4. Offer ladder

Prices in £ first, rand in brackets. Delivery costs from `money.py` plus my time estimates (unverified).

| Rung | Price | What is included | Our cost to deliver |
|---|---|---|---|
| Free: Rank Board | £0 | One monthly challenge leaderboard for the gym TV and a QR poster, up to 30 members, e.g. "most sessions in November" | £0 cash, about 2 hours setup |
| Pilot | £0 for 6 weeks | Full member app for every member: check-ins, streaks, ranks, team leaderboards, weekly owner report. Signed one-page pilot agreement | About £7 (R150) printing, unverified; about 6 hours |
| Paid | £55 (R1,200) a month SA; £79 (R1,716) a month UK | Everything in the pilot, unlimited members, monthly before-and-after report | About £3 a month per gym plus card fees; about 2 hours a month |
| Premium | £110 (R2,400) a month SA; £149 (R3,236) a month UK | Gym's own branding, city league against other gyms, sponsor slot, lapsed-member list for coaches | Same cash cost; about 3 hours a month |
| Trainer tier (later) | £14 (R300) a month | Ranks and streaks for one trainer's own clients | About 1 hour a month |

Recommendation: **launch with the paid tier only; add premium once 3 gyms ask for the league.** Fewer choices close faster.

Competitors I verified exist (not compared on price): [Leaderboarded](https://leaderboarded.com/group-fitness-challenge/) (free for up to 25 participants), [Virtuagym](https://business.virtuagym.com/blog/gym-gamification/), [Your Digital Lift](https://yourdigitallift.com/how-challenges-keep-members-hooked/). Note what booking system each gym uses (CrossFit Aberdeen uses TeamUp; CrossFit Valley Road's site runs on Big Little Gyms); linking to it later is a selling point.

## 5. First 10 clients plan

Your demo already exists, so pitching starts in week 1. Target: **10 gyms on the free Rank Board or a signed pilot by 22 November 2026** (5 each).

**The rules decide the channels.**
- **Josh, South Africa (POPIA):** companies count as data subjects, electronic marketing needs consent, you may send a non-customer **one** consent request only, and since April 2025 an opt-out does not count as consent ([s69 summary](https://mjkinc.co.za/popia/electronic-marketing-section-69); [2025 amendments](https://mjkinc.co.za/popia/regulations-2025-amendments); secondary sources, check against the Gazette). Phone calls count as electronic communication ([Moonstone](https://www.moonstone.co.za/spam-calls-are-now-electronic-communication-guidance-note-closes-direct-marketing-loophole/)). So: **walk in first, ask permission to follow up, log it.** Use draft B (one message) only for gyms you cannot visit, such as East London and Port Alfred.
- **Cam, Scotland (UK GDPR and PECR, UK-wide):** cold email to limited companies is allowed if you say who you are and offer an opt-out. Sole traders and some partnerships need consent first. Live calls must be screened against TPS and CTPS ([ICO B2B guidance](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/), under review after the Data (Use and Access) Act 2025). Check each gym on Companies House before emailing. A directory lists "Results Gym Aberdeen Ltd" ([gymsfitness.co.uk](https://gymsfitness.co.uk/en/i/22982-results-gym-aberdeen-ltd/)), so it is likely a limited company: confirm on Companies House.

**Pilot timing (your decision):** a 6-week pilot from 9 November ends 20 December. That works in Aberdeen. In Gqeberha it runs into the summer holidays, so the numbers would measure people going away, not the app. I recommend: **Aberdeen pilots start 9 November, so the first paying gym is about 21 December, inside your deadline. Gqeberha runs free Rank Boards through December and starts pilots on 5 January 2027 to catch New Year joiners, so the first SA payment is about 16 February 2027, about 3 weeks past your deadline.**

| Week | Josh (Gqeberha) | Cam (Aberdeen) | Target by Sunday |
|---|---|---|---|
| 1: 26 Oct to 1 Nov | Approve drafts. Visit Lions Bay, Valley Road and CrossFit Algoa with the demo on your phone (script A). Start the consent log | Approve drafts. Visit CrossFit Aberdeen, Results Gym and Kimura (script A2). Check Companies House for every Aberdeen prospect | 6 visits; 3 owners agree to see the 10-minute pitch |
| 2: 2 to 8 Nov | Visit prospects 4 to 8. Set up Rank Boards for any yeses | Pitch owners from week 1; offer the pilot straight away. Email limited companies on the list (draft D) | 4 Rank Boards live; 1 Aberdeen pilot signed |
| 3: 9 to 15 Nov | Send draft B once to East London and Port Alfred boxes. Show Rank Board gyms their first numbers | Aberdeen pilots start. Visit prospects 13 to 19. Post on studio Instagram (draft E) | 2 Aberdeen pilots running |
| 4: 16 to 22 Nov | Offer January pilots to Rank Board gyms (draft F); get signatures now | Weekly owner reports. First Rank Day photos with permission | 10 gyms on board or pilot; kill test scored |

**Drafts.** Every draft marked APPROVAL needs your OK before it goes out. Nothing has been sent. Text in square brackets is filled in per gym.

**A. Josh's walk-in script (spoken, no approval needed):**
"Hi, I'm Josh. My business partner Cam and I build apps for local businesses. We've made a game for gym members: ranks, streaks and a leaderboard on your TV, so people keep showing up. Is the owner around for two minutes? If not, could I leave my number and ask: may I WhatsApp or email them about it? I'll only message if they say yes."

**A2. Cam's walk-in script (spoken, no approval needed):**
"Hi, I'm Cam. My business partner and I build apps for gyms. We've made a game for members: ranks, streaks and a leaderboard on your TV, so people keep showing up. Is the owner in? If not, what's the best way to get ten minutes with them?"

**B. SA one-time consent request, WhatsApp or email (APPROVAL):**
"Hi [gym name] team. I'm Josh from Josh and Cam, a small app studio in Gqeberha. May we send you information about a free member leaderboard for your gym? Reply YES to receive it, or NO and we won't contact you again."
(One message only, no sales content.)

**C. SA follow-up after a YES (APPROVAL):**
"Thanks for saying yes. Short version: a free leaderboard for your gym TV and a QR poster at the door. Members check in, earn streaks and climb ranks. It runs for a month at no cost. Can I show you in 10 minutes this week? I'm free Tuesday or Thursday from 10:00. Reply STOP any time and we'll stop."

**D. UK cold email to a limited company (APPROVAL):**
Subject: A free leaderboard for [gym name]'s members
"Hi [gym name] team. I'm Cam from Josh and Cam, a small app studio based in Aberdeen. We've built a game that keeps gym members consistent: check-in streaks, ranks and a TV leaderboard. We're running it free at a few Aberdeen gyms for 6 weeks from 9 November. Could I pop in and show you in 10 minutes? If you'd rather not hear from us, reply 'unsubscribe' and we won't email again."

**E. Studio Instagram post (APPROVAL, it publishes):**
"Building in public: a rank system for gym members. Bronze to Diamond, earned by showing up, not by who lifts the heaviest. Testing it free with a few gyms in Gqeberha and Aberdeen. DM us if your gym wants in."

**F. Pilot offer (APPROVAL):**
"Hi [owner's first name], thanks for running the Rank Board. In [month], [number] members checked in [number] times. We'd like to run the full app for 6 weeks, free, for all your members, starting [date]. You'd put up the QR poster, mention it in classes, and share your attendance numbers from before and during. If it hits the targets in the attached one-page agreement, it continues at [R1,200 / £79] a month, cancel any time with 30 days' notice. If not, you owe nothing. Can we sign this week?"

**10-minute pitch outline:**
1. (1 min) The problem in their numbers: "How many members did you lose last year? At your price, that's [amount]."
2. (2 min) Demo the member view: check in, streak, rank up.
3. (2 min) Demo the owner view: who hasn't been in for 14 days.
4. (1 min) Why it works: the STEP UP trial, competition in small teams.
5. (1 min) Safety: ranks reward showing up and personal bests, not ego lifting.
6. (1 min) The deal: free board now, free 6-week pilot, paid only if it passes.
7. (2 min) Questions, then ask: "Can we put the board up this week?"

## 6. Pilot terms

- **Length:** 6 weeks, free. Aberdeen from 9 November 2026; Gqeberha from 5 January 2027 (if you accept the timing above).
- **Gym commits to:** QR poster at the door, coaches mention it in at least one class a day in week 1, an attendance export (counts only, no names) for the 8 weeks before and the 6 weeks during, plus the same 6 weeks last year, a 15-minute check-in every 2 weeks, and a separate yes or no on using results publicly.
- **We measure:** % of active members who join; % who check in each week; visits per joining member per week against their own baseline; members with no visit for 14+ days; cancellations.
- **Written pass mark** (in the agreement, signed before day 1): the pilot passes if, by the end of week 6, (a) at least 40% of active members have checked in at least once, (b) at least 25% of active members check in during week 6, and (c) joining members average at least 10% more visits a week than their own baseline. Pass means the paid tier starts in week 7, cancellable with 30 days' notice. Fail means it ends, no charge, and we write down why.

## 7. Keeping the client's customers consistent

- **Check-in at the door:** scan the QR poster. Nothing to type. This is the core number.
- **Weekly streaks, not daily:** each member picks 2, 3 or 4 sessions a week. One "freeze" a month for illness or travel.
- **Ranks Bronze to Diamond:** points mostly from attendance, plus points for beating your own previous best (relative to body weight). No points for absolute weight. Divisions by months of training, and age divisions for gyms like Kimura with a 65+ class.
- **Teams of 3:** weekly team leaderboard, copying the design that worked in the STEP UP trial.
- **Milestones:** 1st, 10th, 25th, 50th and 100th session; a "comeback" badge for returning after 14 days away.
- **New member quest:** 6 weeks of simple tasks (book a class, meet a coach, log a first lift). This matters most for the January joiners.
- **Messages** (the app drafts, the gym sends, only to members who opted in): day 7 with no visit, "Your streak's waiting. Class at 17:30 tonight?"; day 14, the coach gets a prompt to call; on a rank-up, "You hit Gold. Show the front desk for your badge."
- **Monthly Rank Day:** badges handed out in person, photos posted by the gym.
- **Proof:** compare the same members before and during the pilot (visits a week, 14-day lapses, cancellations), and against the same weeks last year to allow for seasons. Comparing joiners with non-joiners flatters us, because keen members join first; report it but don't lead with it.

## 8. Growth loops

- **Two-country league:** Gqeberha against Aberdeen in a monthly consistency challenge. Your split location becomes a story gyms will post about.
- **City league:** premium gyms compete against nearby gyms (e.g. CrossFit SAR against Royal Deeside). Each gym has a reason to invite a rival.
- **Shareable rank cards:** a rank-up makes an Instagram story card with the gym's tag.
- **Bring-a-friend quest:** bonus points when a friend does a trial class. The gym gets leads.
- **Gym referral:** a paying gym gets 1 month free for every gym it refers that pays.
- **Sponsors:** a local supplement shop or physio sponsors the monthly prize and pays the gym. We take no cut at first.
- **Content the client posts:** Rank Day photos and a monthly "most consistent member" post, templated by us.

## 9. Demand kill test

**Test:** pitch all 20 prospects in person (Josh 8, Cam 12) between 26 October and 22 November 2026.
**Pass mark, written before we start:** at least 5 sign the one-page pilot agreement, with the price and pass mark in it, by 22 November. A signed January start counts.
**If it fails:**
- 1 to 4 sign: some pull. Re-run with personal trainers at £14 (R300) a month, 10 pitches, pass mark 3 sign-ups.
- 0 sign: stop. Write down the top 3 objections and move to the next studio idea. Total spent: about £20 (R443) a month for one month.

## 10. Costs and money

Run with `python3 money.py`. SA gyms pay Josh through Paystack (2.9% + R1 plus 15% VAT on the fee, [Paystack support page](https://support.paystack.com/hc/en-us/articles/360009881920-What-are-Paystack-s-transaction-charges), checked 23 October 2026). UK gyms pay Cam through Stripe (1.9% + 20p for business cards, [Stripe support page](https://support.stripe.com/questions/pricing-updates-for-businesses-in-the-united-kingdom), dated 2023; a [March 2026 guide](https://www.wearefounders.uk/stripe-fees-uk-2026/) says unchanged). Mix assumed: half SA, half UK, 1 in 4 on premium.

Fixed monthly costs: Supabase Pro £19 (R408), Vercel Pro £15 (R327), Claude Pro for both of you £40 (R869, unverified), domain £1 (R22), ICO data protection fee for Cam £4 (R94; £52 a year, [tier 1 since February 2025](https://acuitylaw.com/rise-in-ico-fees-data-protection-fees-february/)). **Total £79 (R1,720).**

**Before the first paying gym: about £20 (R443) a month of new spend**, inside your £50 budget. That's Vercel Pro, the domain and the ICO fee, with Supabase on its free plan and assuming you already pay for Claude. Switch to Supabase Pro the day the first gym pays. Vercel's free plan bans commercial use ([third-party summary](https://makerkit.dev/blog/saas/vercel-cost); check vercel.com/pricing).

| Clients | SA / UK / premium | Income | Card fees | Fixed | Per-client costs | Profit | Each partner | Our hours a month |
|---|---|---|---|---|---|---|---|---|
| 10 | 5 / 5 / 2 | £796 (R17,300) | £21 (R459) | £79 (R1,720) | £30 (R652) | £666 (R14,469) | £333 (R7,234) | 20 |
| 20 | 10 / 10 / 4 | £1,593 (R34,600) | £42 (R919) | £79 (R1,720) | £60 (R1,303) | £1,411 (R30,657) | £706 (R15,329) | 40 |
| 50 | 25 / 25 / 12 | £4,108 (R89,219) | £109 (R2,366) | £79 (R1,720) | £150 (R3,258) | £3,770 (R81,875) | £1,885 (R40,938) | 100 |

**Getting paid without registering a company yet:**
- **Josh:** Paystack accepts South African sole proprietors with a bank account, a bank letter under 6 months old, ID and proof of address ([Paystack compliance page](https://support.paystack.com/en/articles/2124418)). The collection cap is either R80,000 or R1,000,000; Paystack's own pages conflict, so check in the dashboard.
- **Cam:** Stripe UK lets individuals sign up as sole traders with ID and a personal bank account (third-party guides; check Stripe's UK sign-up). Cam must register for Self Assessment once gross trading income passes £1,000 in a tax year ([summary of HMRC rules](https://www.bytestart.co.uk/self-employed-tax/trading-allowance/); check gov.uk).
- **Recommendation:** stay unregistered sole traders until 5 gyms pay, then decide with an accountant which country to register a company in. Sign a one-page partnership agreement now (who owns the code, how income and costs split, what happens if one of you leaves).

Not included: income tax, VAT (SA and UK both have turnover thresholds, unverified here), bank fees, Paystack's R3 per payout.

## 11. Risks

| Risk | Type | Workaround | Cost |
|---|---|---|---|
| Cold WhatsApp, email or calls breach POPIA s69 | Legal | Walk in first; one consent request only; consent log | £0 |
| UK sole-trader gyms emailed without consent | Legal | Check Companies House; only email limited companies cold | £0 |
| Not paying the ICO fee once Cam handles member data | Legal | Pay the £52 tier 1 fee before the first Aberdeen pilot | £52 (R1,129) a year |
| Body weight and measurements count as health data (special personal information under POPIA, special category data under UK GDPR) | Legal | Body stats optional, private by default, separate explicit consent, never on leaderboards | £0; a one-off lawyer review is advisable, cost unverified |
| Under-18s on leaderboards (Kimura runs youth classes) | Legal and reputation | 18+ only during pilots | £0 |
| SA members' data stored outside SA (POPIA section 72) and UK data stored outside the UK | Legal | One database in a UK or EU region; say in the privacy notice where data is stored; check the s72 conditions before the first SA pilot | £0; unverified detail |
| Gym and we both handle member data with no contract | Legal | One-page data agreement: the gym owns the data, we process it on its instructions | £0 with a template; lawyer review cost unverified |
| Two partners, two countries, no written agreement | Legal and money | One-page partnership agreement now | £0 with a template |
| Apple rejects a native member app (developers report rejections of white-label fitness apps under guideline 3.1.3, [Apple forum](https://developer.apple.com/forums/thread/825551)) | Platform | Ship as a web app members add to their home screen: no App Store review, no Apple fee (about £79 a year, unverified) | £0 |
| Leaderboards push people into ego lifting and injury | Reputation and legal | Rank on attendance and personal improvement; coach-verified lifts only; disclaimer at sign-up | £0 |
| Using "CrossFit" in our name or marketing | Legal (trade mark) | Never use "CrossFit" in the product name or ads | £0 |
| Small Gqeberha box market (2 CrossFit affiliates listed) | Business | Include studios and functional gyms; add East London and Port Alfred by consent request | £0 |
| SA December holidays distort pilot results | Business | SA pilots start 5 January 2027 | Delays first SA income by about 8 weeks |
| Paystack cap reached or account frozen | Payment | Check the cap on sign-up; register a company before reaching it | £0 now |
| Gym stops paying | Payment | Monthly in advance by card; pause the app 7 days after a missed payment | £0 |
| A pilot fails publicly | Reputation | Pilots are private; results only published with written permission | £0 |

## 12. Portfolio capture

| Stage | Collect | Permission |
|---|---|---|
| Build | Screen recordings of the demo and each new feature | None, it's ours |
| Rank Board | Photo of the board on the gym TV (no faces), number of check-ins | Owner's yes in writing |
| Pilot | Weekly owner report screenshots with names hidden; one 30-second owner video | Separate signed media consent |
| Paid | Before-and-after table (visits per member, 14-day lapses, cancellations), owner quote | Written approval of the exact wording |
| Studio | One case study per city, plus a "Gqeberha against Aberdeen" league story | Owner signs off each final page |

## 13. Next 3 actions

1. **Decide two things on your Sunday call (5 minutes):** January start for Gqeberha pilots, yes or no; and keep-your-own-country's-income, yes or no.
2. **Approve or edit drafts B, D, E and F (15 minutes).**
3. **Walk in with the demo on your phone:** Josh to Lions Bay, Valley Road and CrossFit Algoa; Cam to CrossFit Aberdeen, Results Gym and Kimura. Go at quiet times, 10:00 to 11:30 on a weekday or straight after a Saturday morning class.

---

## Tracker checklist

- [ ] Sunday call: decide SA pilot timing and income split
- [ ] Approve drafts B, D, E, F
- [ ] Consent log sheet set up (Josh)
- [ ] Companies House check for each Aberdeen prospect (Cam)
- [ ] Week 1: 3 visits each
- [ ] Pay ICO fee before first Aberdeen pilot (Cam)
- [ ] One-page partnership agreement signed
- [ ] One-page pilot and data agreement template ready
- [ ] Aberdeen pilots start 9 November 2026
- [ ] 10 gyms on board or pilot by 22 November 2026
- [ ] Kill test scored (5 signed?) on 22 November 2026
- [ ] First Aberdeen payment (about 21 December 2026)
- [ ] Gqeberha pilots start 5 January 2027
- [ ] Switch to Supabase Pro on first payment
- [ ] Case study per city drafted
