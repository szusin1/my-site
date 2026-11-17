import pandas as pd

url = "https://raw.githubusercontent.com/flyaflya/persuasive/main/starwars.csv"
sw = pd.read_csv(url, usecols=["name", "height", "mass", "homeworld", "species"])
print(sw.shape)
print(sw.head())

print(sw.assign(inches=lambda df: df["height"] / 2.54).head())

print(
    sw
    .assign(height_m=lambda df: df["height"] / 100)
    .assign(bmi=lambda df: df["mass"] / df["height_m"] ** 2)
    .head()
)

ship_url = "https://raw.githubusercontent.com/flyaflya/persuasive/main/shipments.csv"
shipments = pd.read_csv(
    ship_url, parse_dates=["plannedShipDate", "actualShipDate"]
).head(4000)
print(shipments.dtypes)

late = shipments.assign(
    is_late=lambda df: df["actualShipDate"] > df["plannedShipDate"]
)
print(late.head(3))

print(late["is_late"].sum())
print(late["is_late"].mean())

prod_url = "https://raw.githubusercontent.com/flyaflya/persuasive/main/productLine.csv"
products = pd.read_csv(prod_url)
merged = late.merge(products, on="partID", how="left")
print(len(late), len(merged))
print(merged["prodCategory"].isna().sum())

by_cat = (
    merged
    .groupby("prodCategory")
    .agg(shipments=("is_late", "count"), lateRate=("is_late", "mean"))
    .sort_values("lateRate")
    .round(3)
)
print(by_cat)

service_by_category = (
    pd.read_csv(ship_url, parse_dates=["plannedShipDate", "actualShipDate"])
    .head(4000)
    .assign(is_late=lambda df: df["actualShipDate"] > df["plannedShipDate"])
    .merge(products, on="partID", how="left")
    .groupby("prodCategory")
    .agg(shipments=("is_late", "count"), lateRate=("is_late", "mean"))
    .sort_values("lateRate")
    .round(3)
)
print(service_by_category)

pairs = (
    merged
    .groupby(["shipID", "prodCategory"])
    .agg(lines=("partID", "count"))
    .reset_index()
)
print(len(pairs))
print(pairs.head(3))

per_order = pairs.groupby("shipID").agg(numCategories=("prodCategory", "count"))
print(len(per_order))
print((per_order["numCategories"] > 1).sum())
print((per_order["numCategories"] > 1).mean())

raw = pd.read_csv(ship_url).head(4000)          # no parse_dates
bad = raw.assign(is_late=lambda df: df["actualShipDate"] > df["plannedShipDate"])
print(raw["plannedShipDate"].dtype)
print(bad["is_late"].sum())