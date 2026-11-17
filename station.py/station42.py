import matplotlib.pyplot as plt

decisionArray = ["A", "B", "C", "D", "E"]
satisfactionArray = [3, 5, 4, 3, 1]

bestUtility = max(satisfactionArray)
colorArray = ["darkorchid" if utilityVal == bestUtility else "lightgrey"
              for utilityVal in satisfactionArray]
print(colorArray)

fig, ax = plt.subplots(figsize=[5, 3.5], layout="constrained")
ax.bar(x=decisionArray, height=satisfactionArray, color=colorArray)
ax.set_xlabel("Decision Alternative")
ax.set_ylabel("Utility")
ax.set_title("Decision B is the Best Alternative")
plt.show()

import pandas as pd

regionArray = ["East", "East", "West", "West", "West"]
plotDF = pd.DataFrame({"decision": decisionArray,
                       "satisfaction": satisfactionArray,
                       "region": regionArray})

fig, axs = plt.subplots(ncols=2, figsize=[8, 3.5], layout="constrained", sharey=True)
for idx, (region, groupDF) in enumerate(plotDF.groupby("region")):
    best = groupDF["satisfaction"].max()
    colors = ["darkorchid" if u == best else "lightgrey" for u in groupDF["satisfaction"]]
    bestLabel = groupDF.loc[groupDF["satisfaction"].idxmax(), "decision"]
    axs[idx].bar(x=groupDF["decision"], height=groupDF["satisfaction"], color=colors)
    axs[idx].set_xlabel("Decision Alternative")
    axs[idx].set_ylabel("Utility")
    axs[idx].set_title(f"{region}: Decision {bestLabel} is Best")
fig.suptitle("The Best Decision Differs by Region")
plt.show()

fig, ax = plt.subplots(figsize=[5, 3.5], layout="constrained")
ax.set_title("Decision B is the Best Alternative")
ax.set_xlabel("Decision Alternative")
ax.set_ylabel("Utility")
for decision, satisfaction in zip(decisionArray, satisfactionArray):
    if satisfaction == bestUtility:
        reco = ax.bar(decision, satisfaction, color="darkorchid", label="Recommended")
    else:
        unwise = ax.bar(decision, satisfaction, color="lightgrey", label="Not recommended")
ax.legend(handles=[reco, unwise])
ax.annotate(text="Consider Decision C if sustainability\nmatters. Utility does not include it.",
            xy=("C", 4.05), xytext=("D", 2.2),
            horizontalalignment="center",
            arrowprops={"arrowstyle": "->"})
plt.show()

import pandas as pd

url = "https://raw.githubusercontent.com/flyaflya/persuasive/main/baseball10.csv"
games = pd.read_csv(url)
print(games.shape)
print(games.head(3))

league = avgDF["totalRuns"].mean()
colorArray = ["darkorchid" if team == "COL" else "lightgrey" for team in avgDF["home"]]

fig, ax = plt.subplots(figsize=[6.5, 7], layout="constrained")
ax.barh(avgDF["home"], avgDF["totalRuns"], color=colorArray)
ax.axvline(league, color="black", linestyle="--", linewidth=1)
ax.set_title("Colorado (COL) Is the Most Run-Friendly Ballpark in 2010")
ax.set_xlabel("Average Runs per Game (both teams)")
ax.set_ylabel("Ballpark (home team)")
ax.annotate(text="COL: 10.59 runs a game,\n21% above the league\naverage of 8.77 (dashed line)",
            xy=(10.59, "COL"), xytext=(2.0, "CHA"),
            arrowprops={"arrowstyle": "->"})
plt.show()

fig, axs = plt.subplots(ncols=2, figsize=[10, 7], layout="constrained", sharex=True)
for idx, year in enumerate(["10", "21"]):
    yearDF = (
        pd.read_csv(f"https://raw.githubusercontent.com/flyaflya/persuasive/main/baseball{year}.csv")
        .assign(totalRuns=lambda df: df["homeScore"] + df["visScore"])
        .drop(columns=["date", "visiting"])
        .groupby("home")
        .mean()
        .sort_values("totalRuns")
        .reset_index()
    )
    colors = ["darkorchid" if team == "COL" else "lightgrey" for team in yearDF["home"]]
    axs[idx].barh(yearDF["home"], yearDF["totalRuns"], color=colors)
    axs[idx].set_title(f"20{year}")
    axs[idx].set_xlabel("Average Runs per Game (both teams)")
axs[0].set_ylabel("Ballpark (home team)")
fig.suptitle("Coors Field (COL) Led Baseball in Runs in 2010 but Ranked Third in 2021")
plt.show()