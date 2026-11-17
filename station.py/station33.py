import numpy as np
rng = np.random.default_rng(seed=42)
n = 100_000

rate = rng.uniform(20, 60, size=n)    # parent first: patients per week
time = rng.gamma(400, 1/rate)         # child second: one time for each simulated rate

for i in range(10):
    print(i + 1, round(rate[i], 1), round(time[i], 1))

    print((time > 15).mean())
print(time.mean())
print(np.quantile(time, [0.05, 0.95]))

rng = np.random.default_rng(seed=3)
n = 100_000

promo = rng.binomial(1, 0.5, size=n)          # parent: 1 = promo day
lam = np.where(promo == 1, 60, 30)            # the dial: 60 on promo days, 30 otherwise
arrivals = rng.poisson(lam)                   # child: one draw per row, using that row's dial

print(arrivals.mean())                        # ~ 45
print((arrivals >= 50).mean())                # P(at least 50 customers) ~ 0.46
print(((arrivals >= 40) & (arrivals <= 50)).mean())   # P(between 40 and 50) ~ 0.08

rng = np.random.default_rng(seed=8)
store_a = rng.normal(220, 30, size=n)
store_b = rng.normal(160, 20, size=n)
total = store_a + store_b                  # deterministic child: plain arithmetic, row by row

print(np.quantile(total, 0.95))            # stock this much and you cover 95% of days: ~ 439

rng = np.random.default_rng(seed=7)
n = 100_000

demand = rng.poisson(190, size=n)          # parent
sold   = np.minimum(demand, 182)           # deterministic child: plain arithmetic
shows  = rng.binomial(sold, 0.93)          # random child, one draw per row

print((shows >= 175).mean())               # P(flight full)      ~ 0.042
print((shows > 175).mean())                # P(bumping needed)   ~ 0.019