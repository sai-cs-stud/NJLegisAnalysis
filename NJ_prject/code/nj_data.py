import requests

url = 'https://apps.bea.gov/api/data'

query={'culture':'British','apikey':'89CA3D8D-BE20-4E45-AAAD-A2931A90FC83'}
r = requests.get(url,data=query)
data = r.json()
if r.ok:
  print(r.status_code)
  for x in data['records']:
    print (x['displayname']+' '+ str(x['birthplace']))
else:
  print(r.status_code+'connection failure')