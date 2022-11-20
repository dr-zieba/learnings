import pandas

df = pandas.read_csv("supermarkets-semi-colons.txt", sep=";")
idIndex = df.set_index("ID")
result = idIndex.drop("State",1)



print(result)
