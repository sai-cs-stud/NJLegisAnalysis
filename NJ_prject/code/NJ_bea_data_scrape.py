import requests

#url = 'https://apps.bea.gov/api/data'

#query = {'UserID':'89CA3D8D-BE20-4E45-AAAD-A2931A90FC83','DataSetName':'Regional','TableName':'SAINC1','Year':'2013','method':'GetData','GeoFIPS':'STATE','LineCode':'3'}

url ='https://apps.bea.gov/api/data?UserID=89CA3D8D-BE20-4E45-AAAD-A2931A90FC83&DataSetName=Regional&TableName=SAINC1&Year=2013&method=GetData&GeoFIPS=STATE&LineCode=3'
r = requests.get(url)
data = r.json()
#print(data)
for x in data['BEAAPI']['Results']['Data']:
  print(x['GeoName'])
#  print(x['BEAAPI']['Request']['Data']['GeoName'])


#if r.ok:
#  print(r.status_code)
#  for x in Results['Data']:
#  	print (x['DataValue'])
#else:
#  print(r.status_code+'connection failure')