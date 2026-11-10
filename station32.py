import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=7)

draws = rng.poisson(6, size=100_000)        # <- change this line and rerun:
# draws = rng.binomial(20, 0.35, size=100_000)
# draws = rng.gamma(2, 1/0.5, size=100_000)
# draws = rng.beta(12, 388, size=100_000)
# draws = rng.standard_t(3, size=100_000)

plt.hist(draws, bins=60)
plt.show()

import numpy as np
rng = np.random.default_rng(seed=42)
n = 100_000

rate = rng.uniform(20, 60, size=n)     # parent first: patients per week
time = rng.gamma(400, 1/rate)          # child: weeks until patient #400

print(time.mean())                      # ~11.0 weeks
print(np.quantile(time, [0.05, 0.95])) # ~[6.8, 18.2] weeks