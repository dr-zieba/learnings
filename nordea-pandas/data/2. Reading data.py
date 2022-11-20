import pandas as pd

pd.set_option('display.max_columns',10)
pd.set_option('display.width',1000)
# pd.set_option('display.min_row', 50)

food_df = pd.read_csv('../data/indian_food.csv', dtype={'cook_time':str})#, usecols=[1,3,4]
# print(food_df.shape)
# print(food_df.head(3))
# print(food_df.info())

# web_csv_df = pd.read_csv('https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv')
# print(web_csv_df)

# reading excel file
# food_excel_df = pd.read_excel('../data/indian_food_excel.xlsx', sheet_name='indian_food')

# reading  sheets from already loaded excel file:
excel_file = pd.ExcelFile('../data/indian_food_excel.xlsx')
first_sheet = pd.read_excel(excel_file, 'indian_food')
second_sheet = pd.read_excel(excel_file, 'Sheet1')

separator_df = pd.read_csv('../data/separator.txt', sep='SEPARATOR', engine='python')
print(separator_df)
