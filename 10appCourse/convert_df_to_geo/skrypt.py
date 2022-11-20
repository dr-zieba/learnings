from geopy.geocoders import ArcGIS
import pandas

df1 = pandas.read_csv("supermarkets.csv")
#print(df1)
nom = ArcGIS()
array = []

for index, row in df1.iterrows():
    cord = f"{row['Address']},{row['City']},{row['State']}"
    cord = nom.geocode(cord)
    long = cord.longitude
    lat = cord.latitude
    array.append([lat,long])
    print(f"Longitude: {long}, Latitude: {lat}")

print(array)
