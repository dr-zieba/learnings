import pandas
from geopy.geocoders import ArcGIS
nom = ArcGIS()

df = pandas.read_csv("supermarkets.csv")
print(df)
df["Address"] = df["Address"] + "," + df["City"] + "," + df["State"]
df["Codes"] = df["Address"].apply(nom.geocode)
print(df)
