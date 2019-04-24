import json
with open('temp.json') as f:
    data=json.load(f)

print("Members in CCA team!!")
for emp in data['CCA']:
    print(emp['firstName'],emp['lastName'])
    
print("\n")
print("Members in CPA team!!")
for emp in data['CPA']:
    print(emp['firstName'],emp['lastName'])
    
print("\n")   
print("Members in Insurance claim team!!")
for emp in data['IC']:
    print(emp['firstName'],emp['lastName'])

