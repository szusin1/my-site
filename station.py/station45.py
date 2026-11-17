import pandas as pd

p_difficulty = {"easy": 0.6, "hard": 0.4}
p_intelligence = {"low": 0.7, "high": 0.3}
p_grade = {
    ("low", "easy"): {"A": 0.30, "B": 0.40, "C": 0.30},
    ("low", "hard"): {"A": 0.05, "B": 0.25, "C": 0.70},
    ("high", "easy"): {"A": 0.90, "B": 0.08, "C": 0.02},
    ("high", "hard"): {"A": 0.50, "B": 0.30, "C": 0.20},
}
rows = []
for d, d_prob in p_difficulty.items():
    for i, i_prob in p_intelligence.items():
        for g, g_prob in p_grade[(i, d)].items():
            rows.append({"difficulty": d, "intelligence": i,
                         "grade": g, "p": d_prob * i_prob * g_prob})
students = pd.DataFrame(rows)
print(students.head(6))

def chance_high(table):
    high = table["intelligence"] == "high"
    return table.loc[high, "p"].sum() / table["p"].sum()

print(round(chance_high(students), 3))
hard = students[students["difficulty"] == "hard"]
print(round(chance_high(hard), 3))
got_b = students[students["grade"] == "B"]
print(round(chance_high(got_b), 3))
got_b_hard = got_b[got_b["difficulty"] == "hard"]
print(round(chance_high(got_b_hard), 3))

url = "https://raw.githubusercontent.com/rmcelreath/"
url += "rethinking/master/data/UCBadmit.csv"
ucb = pd.read_csv(url, sep=";")
ucb = ucb.rename(columns={"applicant.gender": "gender"})
print(ucb.head())
overall = ucb.groupby("gender")[["admit", "applications"]].sum()
overall["rate"] = overall["admit"] / overall["applications"]
print(overall.round(3))

ucb["rate"] = (ucb["admit"] / ucb["applications"]).round(2)
print(ucb.pivot(index="dept", columns="gender", values="rate"))

total = ucb.groupby("gender")["applications"].transform("sum")
ucb["share"] = ucb["applications"] / total
print(ucb.pivot(index="dept", columns="gender", values="share").round(2))