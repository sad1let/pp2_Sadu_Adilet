import json

with open('data.json','r') as file:
    data = json.load(file)
# print(data)
# print("""Interface Status================================================================================""")
for i, k in data["imdata"][0]['l1PhysIf']["attributes"].items():
    if i == 'dn':
        print(k, end="                  ")
    if i == "speed":
        print(k, end="                  ")
    if i == "mtu":
        print(k, end="                  ")