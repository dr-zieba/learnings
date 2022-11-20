import pandas as pd

pd.set_option('display.expand_frame_repr', False)

d_json = pd.read_json(r"C:\Users\zieba\Desktop\python\Nowy folder\Employees.json")
d_json.set_index('ID', inplace = True)
print(d_json[~(d_json.loc[:, "Department"] == "IT")])

