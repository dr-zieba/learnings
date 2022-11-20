import os

for folder, sub, file in os.walk('c:\\Users\\zieba\\Desktop\\python'):
    print('Folder: ' + folder)
    print('Sub dirs: ' + str(sub))
    print('File : ' + str(file))
