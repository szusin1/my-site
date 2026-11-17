import numpy as np

rng = np.random.default_rng(seed=3)
shows = rng.binomial(3, 0.9, size=100_000)  # passengers who showed, per flight
print((shows == 3).mean())                  # ~0.729