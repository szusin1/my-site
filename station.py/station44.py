import numpy as np
import pandas as pd

rng = np.random.default_rng(11)
n = 100
pesticide = rng.binomial(n=1, p=0.5, size=n)
fungus = rng.binomial(n=1, p=0.8 - 0.6 * pesticide)
growth = 10 - 4 * fungus + rng.normal(loc=0, scale=1.5, size=n)
plants = pd.DataFrame({"pesticide": pesticide, "fungus": fungus, "growth": growth})
print(plants.head().round(2))

print(plants.groupby("pesticide")["growth"].mean().round(2))
print(pd.crosstab(plants["pesticide"], plants["fungus"]))

print(plants.groupby(["fungus", "pesticide"])["growth"].agg(["count", "mean"]).round(2))

rng = np.random.default_rng(2026)
n = 1000
competence = rng.normal(loc=0, scale=1, size=n)
charisma = rng.normal(loc=0, scale=1, size=n)
surgeons = pd.DataFrame({"competence": competence, "charisma": charisma})
surgeons["score"] = surgeons["competence"] + surgeons["charisma"]
cutoff = surgeons["score"].quantile(0.9)
surgeons["prestigious"] = surgeons["score"] > cutoff
print(surgeons.head().round(2))
print("cutoff:", round(cutoff, 2))

r_all = surgeons["competence"].corr(surgeons["charisma"])
top = surgeons[surgeons["prestigious"]]
r_top = top["competence"].corr(top["charisma"])
print("all surgeons:", round(r_all, 2))
print("prestigious jobs:", len(top), round(r_top, 2))
rest = surgeons[~surgeons["prestigious"]]
r_rest = rest["competence"].corr(rest["charisma"])
print("everyone else:", len(rest), round(r_rest, 2))