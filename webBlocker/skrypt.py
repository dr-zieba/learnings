from datetime import datetime as dt
import time

redir = "127.0.0.1"
webList = ["www.facebook.com", "www.google.pl", "www.aaa.pl"]
path = r"C:\Windows\System32\drivers\etc\hosts"

while True:
  if  15 < dt.now().hour < 16:
    print("work")
    with open(path, "r+") as file:
      content = file.read()
      for web in webList:
        if web in content:
          pass
        else:
          file.write(redir + " " + web + "\n")
  else:
    print("home")
    with open(path, "r+") as file:
      content = file.readlines()
      file.seek(0)
      for line in content:
        if not any(web in line for web in webList):
            file.write(line)
      file.truncate()
      

  time.sleep(3)
