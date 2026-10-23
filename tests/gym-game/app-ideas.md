# Tally: ideas that work with how gyms already run

Research date: 23 October 2026. Sources are linked; vendor pages are marked as such.

## The finding that shapes everything

Gyms already pay for booking and billing software and many have a door or turnstile system. Tally must sit alongside those, never ask a gym to replace them.

- **Booking software varies.** Glofox, PerfectGym and Magicline list developer APIs with webhooks ([API Tracker: Glofox](https://apitracker.io/a/glofox), [PerfectGym](https://apitracker.io/a/perfectgym), [Magicline](https://apitracker.io/a/magicline)). GymMaster's API needs each gym to switch it on and share a key ([Supergood review, third party](https://supergood.ai/docs/gymmaster-api)). I found no developer documentation for PushPress, Mindbody, TeamUp or Wodify, so treat those as unknown.
- **Door systems vary.** In South Africa, vendors sell biometric and card access tied to gym software (for example [Itensity, vendor](https://itensityonline.com/index.php/shop) and [Matrix COSEC's Viva Gym case study, vendor](https://matrixcomsec.com/case-studies/viva-gym), which used palm-vein readers and RFID). Overseas, Kisi links door entry to gym software so each entry becomes a check-in and frozen memberships lose access ([Kisi and GymPoint, vendor](https://www.getkisi.com/integrations/gympoint)).
- **Phone-tap entry needs approval.** Kisi says its credentials can live in Apple Wallet ([Kisi docs, vendor](https://docs.kisi.io/concepts/credentials)). A developer reports that tap-to-enter Wallet passes need an NFC certificate that Apple must grant ([Apple developer forum](https://developer.apple.com/forums/thread/829630)). Google Wallet's tap feature, Smart Tap, has its own onboarding ([Google](https://developers.google.com/wallet/smart-tap)). **So: a Wallet card with a QR code is easy and works anywhere with a QR scanner; tap-to-enter only works through a gym's existing door partner or after Apple and Google approve it.**
- **Discovery Vitality (SA) already pays members for gym visits.** Points are awarded for verified visits, with some platforms using an hourly-changing QR code and a 30-minute minimum ([Octiv guide, vendor](https://guides.octivfitness.com/octiv-vitality-studio-guide); [Discovery Pay as you Gym](https://www.discovery.co.za/vitality/pay-as-you-gym)). Tally must not look like it competes with that; it adds the game on top.

## Now in the demo

1. **Owner "Set up" screen.** Pick the gym type (class gym, open-floor gym, yoga or pilates studio, personal training studio) and the member app changes: tabs, ranks and features switch on or off. This is the answer to "will it work for my gym?".
2. **Four ways to check in, from no hardware to full integration:** QR poster, an hourly-changing code on a front-desk tablet, the Wallet card at the desk or gate, or the gym's existing door system. A gym can pick several.
3. **"Connect" for booking software and door systems.** Shown as generic categories, not brand names, because no partnership exists yet.
4. **Membership card on Home.** It was hidden under Me; now it's one tap from Home.
5. **Guest passes.** Members send a friend a one-day pass; the owner sees sent, visited and joined. When a guest joins, both get points.

## Ideas for later (not built)

| Idea | Why gyms would want it | Works for | Feasibility |
|---|---|---|---|
| Verified visits only: hourly code or door entry plus a 30-minute minimum | Stops people earning points without training; same pattern Vitality platforms use | All | Easy |
| "Away" streak saver: home or holiday workouts count at half points | SA December holidays and travel break streaks, which is when members drift | All | Easy |
| Pause instead of cancel prompt | When a member asks to cancel, offer a pause; the gym keeps the relationship | All, if billing software allows pauses | Depends on booking software |
| Coach view: today's class with who is new, who is coming back after a gap, who is close to a PB | Coaches greet the right people; small, personal touch that keeps members | Class gyms, PT | Easy |
| Wearable import (Apple Health, Google Health Connect) | Workouts done elsewhere still count for streaks | All | Medium; needs a native app |
| On-demand workout library | Members with a busy week still train; gym content keeps them attached | All | Medium; needs content |
| Sponsor prizes on monthly leaderboards | Local shops pay the gym; we take no cut at first | All | Easy |

## What to say to a gym owner

"You don't change your booking system or your door. Start with a poster and a free leaderboard. If it works, we connect it to what you already have."
