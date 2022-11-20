import pandas as pd

pd.set_option('display.max_columns',10)
pd.set_option('display.width',1000)

food_excel_df = pd.read_excel('indian_food_excel.xlsx', sheet_name='indian_food')

food_excel_df['sum_of_cook_time'] = food_excel_df['prep_time'] + food_excel_df['cook_time']
food_excel_df['time_source'] = food_excel_df['prep_time'].astype(str) + '_' + food_excel_df['course']
# assign new values to choosen column:
# food_excel_df['prep_time'] = food_excel_df['prep_time'].astype(str) + '_' + food_excel_df['course']
# sum of prep time
# print(food_excel_df['prep_time'].sum()) # mean(), median()
# print(food_excel_df.head(4))
# print(food_excel_df['prep_time'].add(5))

"""
create a function that will be able to convert input datafrfame to 5 row dataframe,
and create time column from  prep time and cook time column 
"""

def convert_dataframe(dataframe:pd.DataFrame):
    dataframe = dataframe.head(5)
    dataframe['time'] = dataframe['prep_time'] + dataframe['cook_time']

    return dataframe

#print(convert_dataframe(food_excel_df))
#print(food_excel_df.columns.str.upper())
#print(food_excel_df.head(5))
food_excel_df['name'] = food_excel_df['name'].str.replace('h','H')
food_excel_df['New'] = food_excel_df['name'].str.extract('([A-Z])+.')
#print(food_excel_df)

def f(cond1: int, cond2: str):
    food_excel_df = pd.read_excel('indian_food_excel.xlsx', sheet_name='indian_food')
    food_excel_df = food_excel_df[(food_excel_df['cook_time'] < cond1) & (food_excel_df['state']==cond2)]

    return food_excel_df

print(f(30, 'West Bengal'))



