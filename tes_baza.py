import sqlite3

conn=sqlite3.connect("baza_test.db")
cur=conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS employees\
               (id int primary key not null,\
                first_name varchar(25) not null,\
                last_name varchar(25) not null,\
                department varchar(25) not null,\
                phone varchar(25),\
                address varchar(50),\
                salary int);")

conn.commit()
'''
cur.execute("insert into employees (id, first_name, last_name, department, phone, address, salary) \
                values (1, 'John', 'Smith', 'Sales', '+48111111111', 'Poland', '7000'), \
                       (2, 'Adam', 'Kowalski', 'IT', '+88222222222', 'Sweden', '10000'), \
                       (3, 'Robert', 'Nowak', 'Customer Contact', '+11333333333', 'Germany', '2000');")
conn.commit()
'''
cur.execute("select first_name, last_name from employees;")
result = cur.fetchall()
final_result = [i[0] for i in result]
#print(result)

for row in result:
    print(row[0])
    break


#for row in cur.execute("select first_name from employees;"):
#    print(row[0])
