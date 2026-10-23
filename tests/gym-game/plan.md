# Gym game app: customer-base plan (prompt test run)

Test run of `prompt-v1.md` on the gym game idea, 23 October 2026.
Answers given to the prompt's questions: payer "all of the above", city "all of the above" (Cape Town, Johannesburg, Pretoria, a UK city), budget up to £50 a month, first paying gym within 3 months.

**The answer:** sell to owner-run CrossFit boxes and strength gyms, starting in whichever South African city you and Cam live in. Give them a free monthly leaderboard for the gym TV, turn that into a free 6-week pilot with a written pass mark, then charge £55 (R1,200) a month. Members use it free. Rank members mainly on consistency and personal improvement, not raw weight lifted. Build it as a web app, not an App Store app. On these numbers, 20 paying gyms leaves about £652 (R14,166) a month each, before tax.

**Assumptions I made (change any of them):**
- "All of the above" for the payer: I recommend gyms pay and members use it free. Trainers come later as a cheaper tier. Direct-to-member sales and big chains are parked. Reason: one gym signing gets you 50 to 200 users at once, the owner feels the cost of members leaving, and you do not need an ad budget.
- "All of the above" for the city: start in the one SA city where you can both walk in. The other two SA cities come next by email and WhatsApp once you have one case study. London is remote-only and comes after 3 SA case studies, because UK prices are higher but you cannot visit.
- Exchange rate: £1 = R21.72 (longforecast.com, 9 September 2026). Not today's rate; re-check before quoting a client.

---

## 1. The client in one line

The gym owner pays; the members use it; today they rely on a whiteboard, an Instagram post or a booking app's attendance list, and nobody notices a member drifting away until they cancel.

## 2. Why they would pay

| Figure | Source | Notes |
|---|---|---|
| Average member retention is 66.4% a year, so about 1 in 3 members leaves each year | [Health & Fitness Association, 2025 benchmarking report](https://www.healthandfitness.org/publications/the-2025-hfa-global-report/) (175 companies, 17,000+ facilities) | Global benchmark, not SA-specific |
| Independent single-site UK gyms charge £41.94 a month on average; London averages £74.97 | [LeisureDB State of the UK Fitness Industry 2025, via Health Club Management](https://www.healthclubmanagement.co.uk/health-club-management-news/Industry-metrics-are-at-an-all-time-high-says-LeisureDB-David-Minton/356016) | Peak list prices |
| One SA CrossFit box charges R740 (£34) a month unlimited | [CrossFit Plettenberg Bay booking page](https://cfplett.pike13.com/shop) | A single example; Cape Town, Joburg and Pretoria prices not found online, ask on visits |
| 53% of members say they stopped attending at some point without cancelling | [Zenoti survey](https://www.zenoti.com/es/thecheckin/silent-churn-crisis-2026-gym-membership-data) | Vendor survey, treat as secondary |
| Weekly leaderboards in teams of 3 added 920 steps a day, and were the only game design whose effect lasted after it stopped | [STEP UP randomised trial, JAMA Internal Medicine 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6735420) | Steps, not gym visits, but the best evidence that competition works |

The money problem, calculated in `money.py`: a 100-member SA box at 66.4% retention loses about 34 members a year, worth R298,368 (£13,737) in a year of fees if none are replaced. At £55 (R1,200) a month, the gym breaks even if the app keeps **1.6 members** a month who would otherwise have left. In the UK at £79 a month, it is **1.9 members**.

## 3. Real target list

**How many exist:** CrossFit.com lists 11 affiliates in Cape Town, 8 in Johannesburg and 11 in Pretoria ([CrossFit.com South Africa directory](https://www.crossfit.com/gyms/south-africa), checked 23 October 2026). Those are only CrossFit boxes; independent strength gyms add more but I found **no reliable count**. National SA estimates conflict: about 1,100 operators ([Ken Research](https://www.kenresearch.com/industry-reports/south-africa-fitness-services-market)) versus about 3,500 gyms and studios ([Nexdigm](https://www.nexdigm.com/market-research/insights/blog/south-africa-health-and-fitness-club-industry/)), both unverified. The UK has 7,202 gyms ([LeisureDB 2025](https://www.paf-media.co.uk/leisure-db-releases-the-state-of-the-uk-fitness-industry-report-2025)); the 2026 report reportedly has 7,463 ([Health Club Management](https://www.healthclubmanagement.co.uk/health-club-management-features/Evolving-position/38629), from a photo caption).

**Why boxes first:** class-based, coach-led, members already log lifts on a whiteboard, owner-run so one person decides.

**First 20 prospects** (public business pages only; I left out owners' names and personal numbers on purpose). Confirm each is still trading before visiting.

| # | Name | Area | Public page | Why they fit |
|---|---|---|---|---|
| 1 | The Bloc | Blouberg and Melkbosstrand, Cape Town | [thebloc.co.za](https://thebloc.co.za/) | Two sites, says it is the only box on the West Coast: an inter-site league sells itself |
| 2 | Motley Crew CrossFit | Cape Town | [CrossFit.com page](https://crossfit.com/gym/21609/motley-crew-crossfit) | Owner-run, two listed sites (plus [Seaboard](https://crossfit.com/gym/22424/motley-crew-crossfit-seaboard)) |
| 3 | Black River CrossFit | Cape Town | [CrossFit.com page](https://www.crossfit.com/gym/36304/black-river-crossfit) | Already runs graded programmes (a newcomer course and coloured levels, per a [HelloPeter review](https://www.hellopeter.com/black-river-crossfit/reviews/transforming-lives-through-intense-fitness-black-river-crossfit-5170819)): ranks fit their culture |
| 4 | NorSub CrossFit | Northern Suburbs, Cape Town | [CrossFit.com page](https://www.crossfit.com/gym/15253/norsub-crossfit) | Owner-run single box |
| 5 | CrossFit Camissa | Cape Town | [CrossFit.com page](https://crossfit.com/gym/33714/crossfit-camissa) | Small three-person team, wellness focus: consistency ranks over max lifts suit them |
| 6 | Greenside CrossFit | Greenside, Johannesburg | [greensidecrossfit.co.za](https://greensidecrossfit.co.za/) | Based at a sports club: ready-made wider audience for a league |
| 7 | CrossFit Rising Oak | Fourways, Johannesburg | [crossfitrisingoak.co.za](https://crossfitrisingoak.co.za/) | Positions itself as premium: likely to pay for a premium tier |
| 8 | Northcliff CrossFit | Northcliff, Johannesburg | [CrossFit.com page](https://www.crossfit.com/gym/8111/northcliff-crossfit) | Owner-run, lists WhatsApp contact |
| 9 | CrossFit Kyalami | Kyalami, Johannesburg | [CrossFit.com page](https://www.crossfit.com/gym/5578/crossfit-kyalami) | Owner-run single box |
| 10 | Movement Crew CrossFit | Mulbarton, Johannesburg | [CrossFit.com page](https://crossfit.com/gym/23020/movement-crew-crossfit) | Owner-run, south Joburg: less competition from other tools |
| 11 | CrossFit Pretoria | Rietondale, Pretoria | [crossfitpretoria.com](https://www.crossfitpretoria.com/) | Calls itself Pretoria's longest-running box: long-term members to keep |
| 12 | CrossFit PBM | Waterkloof Ridge, Pretoria | [crossfitpbm.com](https://www.crossfitpbm.com/) | Own website, scalable classes for mixed abilities |
| 13 | RTF Fitness | Lynnwood, Pretoria | [rtffitness.co.za](https://www.rtffitness.co.za/) | Runs CrossFit, BoxFit, strength and adaptive training: several divisions to rank |
| 14 | CrossFit Tijger Valley | Pretoria East | [Facebook page](https://www.facebook.com/crossfittijgervalley/) | Active social page: will share rank cards |
| 15 | CrossFit Taniwha | Pretoria East | [Instagram](https://www.instagram.com/crossfittaniwha/) | Active social page, near Tijger Valley: a local league pair |
| 16 | CrossFit North London | North London | [CrossFit.com page](https://www.crossfit.com/gym/5178/crossfit-north-london) | Large three-room facility, also runs HYROX: many members to retain |
| 17 | CrossFit Bermondsey | Bermondsey, London | [crossfitbermondsey.com](https://www.crossfitbermondsey.com/) | Part of a trio of London boxes: a three-gym league |
| 18 | CrossFit Aldgate | Houndsditch, City of London | [CrossFit.com page](https://www.crossfit.com/gym/12120/crossfit-aldgate) | City office workers: team leaderboards by company |
| 19 | Fit This | Hackney, London | [Playsport page](https://playsport.com/fitthis_ag_c2ba680f) | Independent, run by locals, offers a free taster |
| 20 | Gym Nation London Bridge | Southwark, London | [Strength Register page](https://strengthregister.com/gym/gym-nation-london-bridge) | Strength and powerlifting focus; listing is dated, confirm it still trades |

London city choice is my assumption. Tell me if you meant another UK city.

## 4. Offer ladder

Prices in £ first, rand in brackets. Our delivery costs are from `money.py` plus my time estimates (unverified).

| Rung | Price | What is included | Our cost to deliver |
|---|---|---|---|
| Free: Rank Board | £0 | One monthly challenge leaderboard for the gym TV and a QR poster, up to 30 members, e.g. "most sessions in November" | £0 cash, about 2 hours setup |
| Pilot | £0 for 6 weeks | Full member app for every member: check-ins, streaks, ranks, team leaderboards, weekly owner report. Signed one-page pilot agreement | About £7 (R150) printing, unverified; about 6 hours of our time |
| Paid | £55 (R1,200) a month SA; £79 (R1,716) UK | Everything in the pilot, unlimited members, monthly before-and-after report | About £3 a month per gym plus card fees; about 2 hours a month |
| Premium | £110 (R2,400) a month SA; £149 (R3,236) UK | Gym's own branding, city league against other gyms, sponsor slot on leaderboards, lapsed-member list for coaches | Same cash cost; about 3 hours a month |

Recommendation: **one paid tier at launch, add premium only once 3 gyms ask for the league.** Fewer choices close faster.

Competitors I verified exist (not compared on price): [Leaderboarded](https://leaderboarded.com/group-fitness-challenge/) (free for up to 25 participants), [Virtuagym](https://business.virtuagym.com/blog/gym-gamification/) (gym software with gamification), [Your Digital Lift](https://yourdigitallift.com/how-challenges-keep-members-hooked/) (challenges). Ask each prospect what booking system they use; integrating with it later is a selling point.

## 5. First 10 clients plan

Honest target: **10 gyms on the free Rank Board or a pilot by week 4.** Paying clients start in week 7 or later, after the 6-week pilot, which still fits your 3-month deadline.

**The rules shape the channel.** In South Africa, companies count as data subjects under POPIA, electronic marketing needs consent, you may send a non-customer **one** consent request only, and since April 2025 an opt-out does not count as consent ([POPIA s69 summary](https://mjkinc.co.za/popia/electronic-marketing-section-69); [2025 regulation amendments](https://mjkinc.co.za/popia/regulations-2025-amendments), secondary sources, check against the Gazette). The Information Regulator treats phone calls as electronic communication too ([Moonstone](https://www.moonstone.co.za/spam-calls-are-now-electronic-communication-guidance-note-closes-direct-marketing-loophole/)). So in SA: **walk in first, ask for permission to follow up, and log it.** In the UK, cold email to a limited company is allowed if you identify yourself and offer an opt-out; sole traders and some partnerships need consent; live calls must be screened against TPS and CTPS ([ICO B2B guidance](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/), which the ICO says is under review after the Data (Use and Access) Act 2025). Check Companies House to see if a UK gym is a limited company before emailing.

| Week | You | Cam | Target by Sunday |
|---|---|---|---|
| 1 | Approve drafts B, D and E. Walk into 4 boxes in your city at quiet times (10:00 to 11:30 or 14:00 to 16:00). Use script A | Get Claude to build the Rank Board demo on a phone and a laptop. Set up a consent log (sheet: gym, date, who agreed, channel) | Demo works; 4 visits; 2 permissions to follow up |
| 2 | 4 more visits. Run the 10-minute pitch with anyone who agreed. Offer the free Rank Board | Set up Rank Boards for gyms that say yes. Post 2 build updates on your studio Instagram | 3 Rank Boards live |
| 3 | Visit Rank Board gyms, show their numbers, offer the pilot (draft F). Send draft B to boxes in the other two SA cities, once each | Print QR posters. Collect screenshots for the case study. Send draft D to 5 London limited companies | 2 pilots signed; 6 Rank Boards live |
| 4 | Follow up anyone who gave consent (draft C). 4 more visits | Weekly owner reports for pilots. First "Rank Day" post with gym permission | 10 gyms on board or pilot; 3 pilots running |

**Drafts.** Every draft marked APPROVAL must be approved by you before it goes out. I have not sent anything.

**A. Walk-in script (no approval needed, it is spoken):**
"Hi, I'm Josh. My partner Cam and I build apps for local businesses. We're making a game for gym members: ranks, streaks and a leaderboard on your TV, so people keep showing up. Is the owner around for two minutes? If not, could I leave a card and ask: may I WhatsApp or email them about it? I'll only message if they say yes."

**B. SA one-time consent request, WhatsApp or email (APPROVAL):**
"Hi [Gym name] team. I'm Josh from [studio name], a two-person app studio in [your city]. May we send you information about a free member leaderboard for your gym? Reply YES to receive it, or NO and we won't contact you again."
(One message only. No sales content, per the once-only consent rule.)

**C. SA follow-up after a YES (APPROVAL):**
"Thanks for saying yes. Short version: a free leaderboard for your gym TV and a QR poster at the door. Members check in, earn streaks and climb ranks. It runs for a month at no cost. Can I show you in 10 minutes this week? I'm free Tuesday or Thursday from 10:00. Reply STOP any time and we'll stop."

**D. UK cold email to a limited company (APPROVAL):**
Subject: A free leaderboard for [Gym name]'s members
"Hi [Gym name] team. I'm Josh, co-founder of [studio name], a small app studio. We're building a game that keeps gym members consistent: check-in streaks, ranks and a TV leaderboard. We'd like to run it free at a few London boxes for a month. Would a 10-minute video call be useful? [studio name], [registered address]. If you'd rather not hear from us, reply 'unsubscribe' and we won't email again."

**E. Studio Instagram post (APPROVAL, it publishes):**
"Building in public: a rank system for gym members. Bronze to Diamond, earned by showing up, not by who lifts the heaviest. Looking for 3 boxes in [your city] to test it free. DM us."

**F. Pilot offer email (APPROVAL):**
"Hi [owner first name], thanks for running the Rank Board. In [month] [X] members checked in [Y] times. We'd like to run the full app for 6 weeks, free, for all your members. You'd put up the QR poster, mention it in classes, and share your attendance numbers from before and during. If it hits the targets in the attached one-page agreement, it continues at R1,200 a month. If not, you owe nothing. Can we start on [date]?"

**10-minute pitch outline:**
1. (1 min) The problem in their numbers: "How many members did you lose last year? At R740 a month, that is [x]."
2. (2 min) Demo the member view on your phone: check in, streak, rank up.
3. (2 min) Demo the owner view: who has not been in for 14 days.
4. (1 min) Why it works: the STEP UP trial, competition in small teams.
5. (1 min) Safety: ranks reward consistency and personal bests, not ego lifting.
6. (1 min) The deal: free board now, free 6-week pilot, R1,200 a month only if it passes.
7. (2 min) Questions, then ask: "Can we put the board up this week?"

## 6. Pilot terms

- **Length:** 6 weeks, free.
- **Gym commits to:** QR poster at the door, coaches mention it in at least one class a day in week 1, an attendance export (counts only, no names) for the 8 weeks before and the 6 weeks during, a 15-minute check-in every 2 weeks, and a yes or no on using results publicly (separate permission).
- **We measure:** % of active members who join; % who check in each week; visits per joining member per week against their own 8-week baseline; members with no visit for 14+ days; cancellations.
- **Written pass mark** (goes in the agreement, signed before day 1): the pilot passes if, by the end of week 6, (a) at least 40% of active members have checked in at least once, (b) at least 25% of active members check in during week 6, and (c) joining members average at least 10% more visits a week than their own baseline. Pass means the paid tier starts in week 7 at the agreed price, cancellable with 30 days' notice. Fail means it ends, no charge, and we write down why.

## 7. Keeping the client's customers consistent

These are for the gym's members, which is what makes the gym renew.

- **Check-in at the door:** scan the QR poster. Nothing to type. This is the core number.
- **Weekly streaks, not daily:** each member picks a goal of 2, 3 or 4 sessions a week. One "freeze" a month for illness or travel, so one bad week does not wipe out months.
- **Ranks Bronze to Diamond:** points mostly from attendance, plus points for beating your own previous best (relative to body weight). No points for absolute weight. Divisions by months of training, so beginners can win.
- **Teams of 3:** weekly team leaderboard, copying the design that worked in the STEP UP trial.
- **Milestones:** 1st, 10th, 25th, 50th and 100th session; "comeback" badge for returning after 14 days away.
- **New member quest:** 6 weeks of simple tasks (book a class, meet a coach, log a first lift), because the early months are when people drop off.
- **Messages:** the app drafts, the gym sends, only to members who opted in at sign-up. Day 7 with no visit: "Your streak's waiting. Class at 17:30 tonight?" Day 14: coach gets a prompt to call. Rank-up: "You hit Gold. Show the front desk for your badge."
- **Monthly Rank Day:** badges handed out in person, photos posted by the gym.
- **Proof:** compare the 8 weeks before against the 6 pilot weeks for visits per member, 14-day lapses and cancellations. Also compare joiners with non-joiners, with a warning that keen members join first, so that comparison flatters us. The before-and-after on the same members is the honest one.

## 8. Growth loops

- **City league:** premium gyms compete against other gyms in monthly challenges. Each gym has a reason to invite a rival, and the rival needs the app to enter.
- **Shareable rank cards:** a rank-up makes an Instagram story card with the gym's tag. Members advertise the gym and the app.
- **Bring-a-friend quest:** bonus points when a friend does a trial class. The gym gets leads, which it values more than the game.
- **Gym referral:** a paying gym gets 1 month free for every gym it refers that pays.
- **Sponsors:** a local supplement shop or physio sponsors the monthly prize. The sponsor pays the gym; the gym is happier to renew. We take no cut at first.
- **Content the client posts:** Rank Day photos and a monthly "most consistent member" post, which we template for them.

## 9. Demand kill test

**Test:** pitch the free Rank Board and pilot, in person, to 15 gym owners over weeks 1 to 3.
**Pass mark, written before we start:** at least 5 of 15 sign the one-page pilot agreement, with the R1,200 price and pass mark in it, by the end of week 4.
**If it fails:**
- 1 to 4 sign: the idea has some pull. Re-run with personal trainers at £14 (R300) a month for their own clients, 10 pitches, pass mark 3 sign-ups.
- 0 sign: stop. Write down the top 3 objections and move to the next studio idea. Total cost so far: about £16 (R348) and 3 weeks.

## 10. Costs and money

Run with `python3 money.py`. All billing through Paystack in rand (2.9% + R1 for SA cards, 3.1% + R1 for foreign cards, plus 15% VAT on the fee, from the [Paystack support page](https://support.paystack.com/hc/en-us/articles/360009881920-What-are-Paystack-s-transaction-charges), checked 23 October 2026). Mix assumed: 1 in 5 clients in the UK, 1 in 4 on premium.

Fixed monthly costs: Supabase Pro £19 (R408), Vercel Pro £15 (R327), Claude Pro for both of you £40 (R869, unverified), domain £1 (R22). **Total £75 (R1,626).**

| Clients | SA / UK / premium | Income | Card fees | Fixed | Per-client costs | Profit | Each partner | Our hours a month |
|---|---|---|---|---|---|---|---|---|
| 10 | 8 / 2 / 2 | £710 (R15,432) | £25 (R534) | £75 (R1,626) | £30 (R652) | £581 (R12,620) | £291 (R6,310) | 20 |
| 20 | 16 / 4 / 5 | £1,491 (R32,384) | £52 (R1,122) | £75 (R1,626) | £60 (R1,303) | £1,304 (R28,333) | £652 (R14,166) | 40 |
| 50 | 40 / 10 / 12 | £3,692 (R80,200) | £128 (R2,779) | £75 (R1,626) | £150 (R3,258) | £3,340 (R72,537) | £1,670 (R36,269) | 100 |

**Budget warning:** £75 is over your £50 limit. Before the first paying gym, run on Supabase's free plan and only pay for Vercel Pro (£15) and the domain (£1): about **£16 (R348) a month of new spend**, assuming you already pay for Claude. Switch to Supabase Pro on the day the first gym pays. Vercel's free plan bans commercial use, so it is not an option even during free pilots ([third-party summary](https://makerkit.dev/blog/saas/vercel-cost); check vercel.com/pricing).

Not included: income tax, VAT registration (SA requires it above a turnover threshold, unverified), bank fees, and Paystack's R3 per payout.

## 11. Risks

| Risk | Type | Workaround | Cost |
|---|---|---|---|
| Cold WhatsApp, email or calls breach POPIA s69 | Legal | Walk in first, one consent request only, consent log | £0 |
| UK sole-trader gyms emailed without consent | Legal | Check Companies House; only email limited companies cold | £0 |
| Body weight and measurements count as health data (special personal information under POPIA, special category data under UK GDPR) | Legal | Body stats optional, private by default, separate explicit consent; never shown on leaderboards | £0 build time; a one-off lawyer review is advisable, cost unverified |
| Under-18 members on public leaderboards | Legal and reputation | 18+ only during pilots | £0 |
| Gym and we both handle member data with no contract | Legal | One-page data agreement: gym owns the data, we process it on their instructions | £0 with a template; lawyer review cost unverified |
| Apple rejects a native member app (developers report rejections of white-label fitness apps under guideline 3.1.3, [Apple forum](https://developer.apple.com/forums/thread/825551)) | Platform | Ship as a web app members add to their home screen: no App Store, no review, no £79 a year Apple fee | £0 |
| Leaderboards push people into ego lifting and injury | Reputation and legal | Rank on attendance and personal improvement; coach-verified lifts only; disclaimer at sign-up | £0 |
| Using "CrossFit" in our name or marketing | Legal (trade mark) | Never use "CrossFit" in the product name or ads; refer to "boxes" or "gyms" | £0 |
| Gym stops paying | Payment | Monthly in advance by card or Paystack EFT (2% fee); pause the app 7 days after a missed payment | £0 |
| Exchange rate moves against rand pricing for UK gyms | Payment | Re-price UK clients yearly; quote in £ | £0 |
| A pilot fails publicly | Reputation | Pilots are private; results only published with written permission | £0 |

## 12. Portfolio capture

| Stage | Collect | Permission |
|---|---|---|
| Build | Screen recordings of the app at each milestone, before and after designs | None, it is ours |
| Rank Board | Photo of the board on the gym TV (no faces), number of check-ins | Owner's yes in writing |
| Pilot | Weekly owner report screenshots with names hidden; one 30-second owner video | Separate signed media consent |
| Paid | Before-and-after table (visits per member, 14-day lapses, cancellations), owner quote | Written approval of the exact wording |
| Studio | One-page case study: problem, what we built, result, quote | Owner signs off the final page |

## 13. Next 3 actions

1. **Tell me your city and studio name** (2 minutes), so the drafts and the visit list are final.
2. **Approve or edit drafts B, D and E** (15 minutes).
3. **Ask Claude to build the free Rank Board demo**, then walk into 4 boxes on Saturday between 09:00 and 11:00.

---

## Tracker checklist

- [ ] Confirm home city and studio name
- [ ] Approve drafts B, D, E (Josh)
- [ ] Build Rank Board demo (Cam with Claude)
- [ ] Set up consent log sheet (Cam)
- [ ] Week 1: 4 gym visits (Josh)
- [ ] Week 2: 3 Rank Boards live
- [ ] Week 3: 2 pilots signed with written pass mark
- [ ] Week 4: 10 gyms on board or pilot
- [ ] Kill test result recorded (5 of 15 signed?)
- [ ] Pilot week 6 pass or fail recorded per gym
- [ ] First paying gym (target: by 23 January 2027)
- [ ] Switch to Supabase Pro on first payment
- [ ] Case study page drafted
