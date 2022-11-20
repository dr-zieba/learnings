import sys, os

if len(sys.argv)-1!=1:
    print("Provide path arg in cmd!")
    sys.exit()

path = sys.argv[1]

try:
    print(f"Current directiory: {os.getcwd()}")
    os.chdir(path)
except Exception as e:
    print(e)
finally:
    print(f"Directory changed to: {os.getcwd()}")
