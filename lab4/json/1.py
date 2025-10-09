import json
with open('sample-data.json','r') as file:
    data=json.load(file)
things=data['imdata']
print("Interface Status")
print("="*80)
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
for i in things:
    print(i["l1PhysIf"]["attributes"]["dn"]," "*29,i["l1PhysIf"]["attributes"]["speed"]," "*1,i["l1PhysIf"]["attributes"]["mtu"])