import requests
import json

query = {'lat':'45', 'lon':'180'}
request = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
if request.status_code == 200:
    resp = request.json()
    print(resp['response'][1]['duration'])
    print(f"Status code: {request.status_code}")
else:
    print(f"Status code: {request.status_code}")

