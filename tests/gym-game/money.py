"""Costs and income for the gym game app at 10, 20 and 50 paying clients.

Every input is listed at the top with its source or "unverified".
Run: python3 money.py
"""

# Exchange rates (stale, not today's rate: re-check before quoting to a client)
ZAR_PER_GBP = 21.72   # longforecast.com, 9 Sep 2026
GBP_PER_USD = 0.7523  # poundsterlinglive.com, 28 Jul 2026

# Prices we charge (our choice, monthly)
SA_PAID_ZAR = 1200
SA_PREMIUM_ZAR = 2400
UK_PAID_GBP = 79
UK_PREMIUM_GBP = 149

# Client mix (assumption): Josh sells in Gqeberha, Cam sells in Aberdeen
SHARE_UK = 0.50       # half the clients in the UK, half in SA
SHARE_PREMIUM = 0.25  # 1 in 4 clients on premium

# Card fees
# SA gyms pay Josh through Paystack: support page, fetched 23 Oct 2026
VAT = 0.15                      # SA VAT, charged on Paystack's fee
LOCAL_PCT, LOCAL_FLAT = 0.029, 1.00   # SA cards, VAT exclusive
# UK gyms pay Cam through Stripe UK. Business cards: Stripe support page (2023),
# a March 2026 guide says unchanged. Using the business-card rate to be safe.
UK_PCT, UK_FLAT_GBP = 0.019, 0.20

# Fixed monthly running costs in GBP
FIXED_GBP = {
    "Supabase Pro database ($25, third-party 2026 guides)": 25 * GBP_PER_USD,
    "Vercel Pro hosting, 1 seat ($20, third-party 2026 guides)": 20 * GBP_PER_USD,
    "Claude Pro x2 (GBP 20 each, aggregator, unverified)": 40,
    "Domain (about GBP 12 a year, unverified)": 1,
    "ICO data protection fee for Cam (GBP 52 a year, tier 1 from Feb 2025)": 52 / 12,
}
# Before the first paying gym: Supabase free plan, so these are the only new costs
PRE_REVENUE_KEYS = [k for k in FIXED_GBP if k.startswith(("Vercel", "Domain", "ICO"))]

# Costs that grow with clients (GBP per client per month, unverified estimates)
VARIABLE_GBP_PER_CLIENT = {
    "Extra database and hosting usage": 1.0,
    "Printed QR posters and badges": 2.0,
}
# Our time per client per month, not a cash cost but shown so we price honestly
HOURS_PER_CLIENT = 2


def fee_zar(amount_zar, pct, flat):
    return (amount_zar * pct + flat) * (1 + VAT)


def month(clients):
    uk = round(clients * SHARE_UK)
    sa = clients - uk
    uk_prem = round(uk * SHARE_PREMIUM)
    sa_prem = round(sa * SHARE_PREMIUM)
    uk_paid, sa_paid = uk - uk_prem, sa - sa_prem

    # SA billed in rand through Paystack, UK billed in pounds through Stripe
    sa_rows = [(sa_paid, SA_PAID_ZAR), (sa_prem, SA_PREMIUM_ZAR)]
    uk_rows = [(uk_paid, UK_PAID_GBP), (uk_prem, UK_PREMIUM_GBP)]

    gross = sum(n * p for n, p in sa_rows) / ZAR_PER_GBP + sum(n * p for n, p in uk_rows)
    fees = sum(n * fee_zar(p, LOCAL_PCT, LOCAL_FLAT) for n, p in sa_rows) / ZAR_PER_GBP
    fees += sum(n * (p * UK_PCT + UK_FLAT_GBP) for n, p in uk_rows)
    fixed = sum(FIXED_GBP.values())
    variable = clients * sum(VARIABLE_GBP_PER_CLIENT.values())
    profit = gross - fees - fixed - variable
    return {
        "clients": clients, "sa": sa, "uk": uk, "premium": sa_prem + uk_prem,
        "gross": gross, "fees": fees, "fixed": fixed, "variable": variable,
        "profit": profit, "each": profit / 2, "hours": clients * HOURS_PER_CLIENT,
    }


def money(gbp):
    return f"£{gbp:,.0f} (R{gbp * ZAR_PER_GBP:,.0f})"


if __name__ == "__main__":
    print("Fixed monthly costs:")
    for k, v in FIXED_GBP.items():
        print(f"  {k}: {money(v)}")
    print(f"  Total fixed: {money(sum(FIXED_GBP.values()))}")
    print(f"  Before the first paying gym: {money(sum(FIXED_GBP[k] for k in PRE_REVENUE_KEYS))}\n")

    header = "| Clients | SA / UK / premium | Income | Card fees | Fixed | Per-client costs | Profit | Each partner | Our hours |"
    print(header)
    print("|" + "---|" * 9)
    for n in (10, 20, 50):
        m = month(n)
        print(f"| {n} | {m['sa']} / {m['uk']} / {m['premium']} | {money(m['gross'])} | {money(m['fees'])} "
              f"| {money(m['fixed'])} | {money(m['variable'])} | {money(m['profit'])} | {money(m['each'])} | {m['hours']} |")

    # Payback for the gym: how many members must the app keep to cover its price
    box_fee_zar = 740  # CrossFit Plettenberg Bay unlimited monthly, Pike13 page
    print(f"\nGym payback (SA paid tier R{SA_PAID_ZAR}/month vs a R{box_fee_zar}/month member): "
          f"keeping {SA_PAID_ZAR / box_fee_zar:.1f} members who would otherwise leave covers it.")
    uk_fee = 41.94  # LeisureDB 2025, independent single-site average
    aberdeen_fee = 99  # CrossFit Aberdeen strength-area-only unlimited, TeamUp page
    print(f"Gym payback (UK paid tier £{UK_PAID_GBP}/month vs a £{uk_fee}/month member): "
          f"keeping {UK_PAID_GBP / uk_fee:.1f} members who would otherwise leave covers it.")
    print(f"Gym payback (UK paid tier £{UK_PAID_GBP}/month vs a £{aberdeen_fee}/month Aberdeen member): "
          f"keeping {UK_PAID_GBP / aberdeen_fee:.1f} members who would otherwise leave covers it.")
    members, retention = 100, 0.664  # HFA 2025 benchmark retention
    lost = members * (1 - retention)
    print(f"A 100-member SA box at 66.4% retention loses about {lost:.0f} members a year, "
          f"worth R{lost * box_fee_zar * 12:,.0f} (£{lost * box_fee_zar * 12 / ZAR_PER_GBP:,.0f}) "
          f"in a year of fees if none are replaced.")
