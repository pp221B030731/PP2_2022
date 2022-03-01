import json

with open("sample-data.json") as x:
	s = json.load(x)
print("Interface Status \n================================================================================\nDN                                                 Description           Speed    MTU  \n-------------------------------------------------- --------------------  -------  ------")
for i in s['imdata']:
	print(i['l1PhysIf']['attributes']['dn'], (48-len(i['l1PhysIf']['attributes']['dn']))*' ', i['l1PhysIf']['attributes']['descr'], (21-len(i['l1PhysIf']['attributes']['descr']))*' ', i['l1PhysIf']['attributes']['speed'], (6 - len(i['l1PhysIf']['attributes']['speed']))*' ', i['l1PhysIf']['attributes']['mtu'])
		

