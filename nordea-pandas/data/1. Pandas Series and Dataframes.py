import pandas as pd

# https://pandas.pydata.org/docs/user_guide/index.html

# creation of dataframe
#1. example
df = pd.DataFrame({'name': ['adam','joe','maria'],
                   'surname': ['surname1','surname2','surname3']},
                  index=['male','male','female'])
# 2. example
df2 = pd.DataFrame(data=[['adam','surname1'],
                         ['joe','surname2'],
                         ['maria','surname2']],
                   columns=['name','surname'],
                   index=['male','male','female'])
# print(type(df2))
# print(df2.head(100))
# print(len(df2))
# print(df2.shape)
# print(df2.columns)

#convert to dictionary
# print(df2.to_dict())
test_dict = {'name2': {'male': 'joe', 'female': 'maria'},
             'surname2': {'male': 'surname2', 'female': 'surname2'}}
#covert from dictionary
from_dicrionary_df = pd.DataFrame.from_dict(test_dict)
# print(from_dicrionary_df)

# Pandas dtypes: https://pbpython.com/pandas_dtypes.html
# print(df2.dtypes)
# print(df2.info())

#assign value to selected column
df2['name'] = 'Adam'
# print(df2)
df1 = pd.DataFrame({'a':[10,20,30], 'b': [20,30,40]})
# print(df1)
df_new = df1.copy()
df1['a'] = df1['a'] + 1
# print(df_new)
# print(df1)

# pandas series
# print(type(df1[['b']]))
sr = pd.Series(data=['Piotr', 'Adam', 'Maria', 'Michał'], name='nanan')
# print(sr.tolist())
#convert from list to pd Series
data_list = ['Piotr', 'Adam', 'Maria', 'Michał']
series = pd.Series(data_list)
# print(series)
#convert to dataframe from series
# print(type(sr.to_frame()))

print(df1)
df1['c'] = sr
print(df1)
