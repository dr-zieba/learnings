import psycopg2

try:
    connection = psycopg2.connect(database="staff",\
                                  user="jan",\
                                  password="python",\
                                  host="127.0.0.1",\
                                  port="5433")
except psycopg2.Error as err:
    print("Connection faild")
else:
    print("Connected!!!")

cursor = connection.cursor()
'''cursor.execute("create table mystaff.employees\
               (id int primary key not null,\
                first_name varchar(25) not null,\
                last_name varchar(25) not null,\
                department varchar(25) not null,\
                phone varchar(25),\
                address varchar(50),\
                salary int);")
'''
cursor.execute("insert into mystaff.employees (id, first_name, last_name, department, phone, address, salary) \
                values (1, 'John', 'Smith', 'Sales', '+48111111111', 'Poland', '7000'), \
                       (2, 'Adam', 'Kowalski', 'IT', '+88222222222', 'Sweden', '10000'), \
                       (3, 'Robert', 'Nowak', 'Customer Contact', '+11333333333', 'Germany', '2000');")
connection.commit()
'''cursor.execute("update mystaff.employees set department = 'IT' where first_name = 'John' and last_name = 'Smith';")
'''
'''cursor.execute("delete from mystaff.employees where first_name = 'John' and last_name = 'Smith';")
'''
cursor.execute("select * from mystaff.employees;")
result = cursor.fetchall()
#result2 = cursor.fetchone()
#for row in result:
#    print(row)

print(result)


connection.close()

