import mysql.connector
from difflib import get_close_matches

'''
conn = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = conn.cursor()
query = cursor.execute("select * from Dictionary where Expression='acid'")
result = cursor.fetchall()

for row in result:
    print(row)
    print("\n")
'''
def search(input):

    try:
        conn = mysql.connector.connect(
        user = "ardit700_student",
        password = "ardit700_student",
        host = "108.167.140.122",
        database = "ardit700_pm1database"
        )
        cursor = conn.cursor()
        query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression='{input}'")
        result = cursor.fetchall()

        if result:
            for row in result:
                print(row)
        else:
            print("Not found")
    except Exception as e:
        print("Error", e)



user_input = input("Search for: ")
search(user_input)
