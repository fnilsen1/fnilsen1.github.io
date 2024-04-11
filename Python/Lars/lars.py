# import json

# with open('fnilsen1.github.io\Python\Lars\lars.json', 'r') as file:
#     data = json.load(file)


# people_id = {



# }
# podiums = {

# }

# for i in data["persons"]:
#     people_id[i["registrantId"]] = i["email"]

# for i in data["events"]:
#     podiums[i["id"]]=[]
#     for j in range(3):
#         podiums[i["id"]].append(people_id[i["rounds"][-1]["results"][j]["personId"]])
        
# print(podiums)

# a=[1,2,5,14,42,132,429,1430,4862,16796,58786]
# b=[0,1]
# for i in range(24):b.append(b[i]+b[i+1])
# for i in range(1,100000):
#     if (i in a or i in b) and i not in set(a)&(set(b)):print(i)
