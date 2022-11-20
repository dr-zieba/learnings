import pandas as pd

excel_file = pd.read_csv('/home/jan/Desktop/python/nordea-pandas/data/indian_food.csv', usecols=[1,3,4])
excel_file = excel_file.iloc[3:14]
'''
file = excel_file[(excel_file['cook_time'] <= 40)]
file.to_excel('test.xlsx', index=False, sheet_name="qwe")
print(file)
'''

def create_file(path: str, df: pd.DataFrame, colums_name: str, clumn_values: int):
    '''
    :param path:
    :param df:
    :param colums_name:
    :param clumn_values:
    :return:
    '''
    file = df[df[colums_name] <= clumn_values]
    file.to_excel(path, index=False)

create_file('test2.xlsx', excel_file, 'cook_time', 30)
