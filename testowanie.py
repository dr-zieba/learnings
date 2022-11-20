import os, platform

# Get the list of all files and directories
# in the root directory
'''
path = "C:\\Users\\zieba\\Desktop\\python\\testowanie.py"

print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))
print(os.path.exists(path))

x = "katalog2"
y = "file.txt"

print(os.path.join(x, y))

if os.system("dirq")==0:
    print("success")
else:
    print("Failed")

os_version = platform.system()
print(os_version)

if os_version == "Windows":
    os.system("cls")
elif os_version == "Linux":
    os.system("clear")
else:
    print("Unknown os system version")
'''
'''
path = "C:\\Users\\zieba\\Desktop\\python\\biblioteka"

for x,y,z in list(os.walk(path)):
    if len(z) == 0:
        print(f"Directories: {x}/{y} and files: {z}\n")
'''

l1 = [1,2,3]
l1_copy =[]

for i in l1:
    l1_copy.append(i)

print(l1_copy, id(l1), id(l1_copy))
print("---------")

l2_copy = [i for i in l1]
print(l2_copy)




















