import pandas

df1 = pandas.read_csv("supermarkets.csv")
#print(df1)
df1.columns=["ID","Adr","State","City","Coutry","Name","Emp"]
#print(df1)
df1.set_index("ID", inplace=True)
print(df1.loc[1:2,"Adr":"City"])

'''
from geopy.geocoders import ArcGIS
nom = ArcGIS()
'''
