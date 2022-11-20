from sqlalchemy import create_engine
import pandas as pd

d_txt = pd.read_csv(r"C:\Users\zieba\Desktop\python\app266\my_employees.txt")
d_csv = pd.read_csv(r"C:\Users\zieba\Desktop\python\app266\my_employees.csv")
d_json = pd.read_json(r"C:\Users\zieba\Desktop\python\app266\my_employees.json")
d_xlsl = pd.read_excel(r"C:\Users\zieba\Desktop\python\app266\my_employees.xlsx", sheet_name = 0)

engine = create_engine('postgresql+psycopg2://jan:python@127.0.0.1:5433/staff')
dsql = pd.read_sql_table('employees', engine, schema = 'mystaff')

dsql.rename({"id": "ID", "first_name": "FirstName", "last_name": "LastName", "department": "Department",
             "phone": "Phone", "address": "Address", "salary": "Salary"}, axis = 'columns', inplace = True)

d_txt.to_sql('all', engine, schema = 'mystaff', index = False, if_exists = 'append')
d_csv.to_sql('all', engine, schema = 'mystaff', index = False, if_exists = 'append')
d_json.to_sql('all', engine, schema = 'mystaff', index = False, if_exists = 'append')
d_xlsl.to_sql('all', engine, schema = 'mystaff', index = False, if_exists = 'append')

query_all = pd.read_sql_query('select * from mystaff.all', engine)

guery_count = pd.read_sql_query('select count("ID") from mystaff.all', engine)
total_empolyees = guery_count.iloc[0][0]
print(total_empolyees)

query_dept = pd.read_sql_query('select count(distinct "Department") from mystaff.all', engine)
total_dept = query_dept.iloc[0][0]
print(total_dept)

guery_employees_per_dept = pd.read_sql_query('select "Department", count("ID") from mystaff.all group by "Department"', engine)
print(guery_employees_per_dept)


query_dept_list = pd.read_sql_query('select distinct "Department" from mystaff.all', engine)


summary = [["Nr of employees: ", int(total_empolyees)],
           ["Nr department: ", total_dept],
           ["Dept list: ", query_dept_list]]
           
summary_html = pd.DataFrame(summary, columns = ["Stats", "Values"])

with open(r"C:\Users\zieba\Desktop\python\app266\my_employees.html", "w") as f:
    summary_html.to_html(f, index = False, justify = 'center')
