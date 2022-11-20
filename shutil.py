import shutil, os, send2trash

shutil.copy('C:\\Users\\zieba\\Desktop\\python\\text.txt', 'C:\\Users\\zieba\\Desktop\\python\\skopiowany.txt')
send2trash.send2trash('C:\\Users\\zieba\\Desktop\\python\\skopiowany.txt')
#shutil.copytree('C:\\Users\\zieba\\Desktop\\python', 'C:\\Users\\zieba\\Desktop\\python2')
