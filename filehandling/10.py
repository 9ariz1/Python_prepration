import json

file=open('n.json','r')
data=json.load(file)
print(data['users'][1]['firstName'],data['users'][1]['lastName'])
file.close()