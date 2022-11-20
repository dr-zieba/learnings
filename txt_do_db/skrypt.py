from psycopg2 import *

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

plik_employees = open(r'C:\Users\zieba\Desktop\python\txt_do_db\employees.txt', 'r')

tekst = plik_employees.readlines()

for line in tekst:
    query = ', '.join("'" + item + "'" for item in line.strip().split('/ '))
    print(query)
    cursor.execute("INSERT INTO mystaff.employees VALUES ({});".format(query))

connection.commit()
connection.close()
