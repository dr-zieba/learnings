import wikipedia
import requests
import os.path

page = wikipedia.page("beach")

#url = page.images[3]
url = "https://upload.wikimedia.org/wikipedia/commons/b/bf/Aegopodium_podagraria1_ies.jpg"

print(url)
print(os.path.basename(url))
img_path = f"test/{os.path.basename(url)}"
r = requests.get(url, stream=True)

with open(img_path, 'wb') as f:
    f.write(r.content)