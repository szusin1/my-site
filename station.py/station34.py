import numpy as np
rng = np.random.default_rng()          # no seed: this path is yours alone

flips = rng.binomial(1, 0.5, size=10)  # ten coin flips: 1 = heads, 0 = tails
print(flips)
print(30_000 * np.where(flips == 1, 1.5, 0.6).prod())   # your balance after 10 years

rng = np.random.default_rng(seed=42)
n_paths, years = 100_000, 30

flips = rng.binomial(1, 0.5, size=(n_paths, years))     # 1 = heads; one row per investor
factors = np.where(flips == 1, 1.5, 0.6)                # +50% or -40%
final = 30_000 * factors.prod(axis=1)                   # multiply across each row

print(f"mean:   ${final.mean():>12,.0f}")     # ~ $124,000  (near the promised EV)
print(f"median: ${np.median(final):>10,.0f}")  # ~ $6,200    (the typical investor)
print(f"P(ending below the $30k buy-in): {(final < 30_000).mean():.2f}")   # ~ 0.71

rng = np.random.default_rng(seed=7)
flips = rng.binomial(1, 0.5, size=(100_000, 30))
for f in [0.0, 0.10, 0.25, 0.50, 1.00]:
    factors = np.where(flips == 1, 1 + 0.5*f, 1 - 0.4*f)
    final = 30_000 * factors.prod(axis=1)
    print(f"f = {f:.2f}   median ${np.median(final):>9,.0f}   P(loss) {(final < 30_000).mean():.2f}")