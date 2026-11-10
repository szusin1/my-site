# recipe shape: parents before children
import numpy as np
rng = np.random.default_rng(seed=0)
first = rng.binomial(1, 0.52, size=100_000)
lam = np.where(first == 1, 47, 26)
x = rng.poisson(lam)
print((x >= 35).mean())