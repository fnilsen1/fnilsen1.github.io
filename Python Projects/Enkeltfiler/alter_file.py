z_dict = {
"R": "D",
"R'": "D'",
"R2": "D2",
"L": "U",
"L'": "U'",
"L2": "U2",
"U": "R",
"U'": "R'",
"U2": "R2",
"D": "L",
"D'": "L'",
"D2": "L2",
"F": "F",
"F'": "F'",
"F2": "F2",
"B2": "B2",
}

zp_dict = {
"R": "U",
"R'": "U'",
"R2": "U2",
"L": "D",
"L'": "D'",
"L2": "D2",
"U": "L",
"U'": "L'",
"U2": "L2",
"D": "R",
"D'": "R'",
"D2": "R2",
"F": "F",
"F'": "F'",
"F2": "F2",
"B2": "B2",
}

z2_dict = {
"R": "L",
"R'": "L'",
"R2": "L2",
"L": "R",
"L'": "R'",
"L2": "R2",
"U": "D",
"U'": "D'",
"U2": "D2",
"D": "U",
"D'": "U'",
"D2": "U2",
"F": "F",
"F'": "F'",
"F2": "F2",
"B2": "B2",
}

def insert_moves(alg):
    alg = alg.strip()
    z_count = 0

#R2 U2 R' F2 R2 U2 R' B F' U2 B' F' R2 U2 R' F2
    alg = alg.replace("F B'", "S'")
    alg = alg.replace("B F'", "S")
    alg = alg.replace("B' F ", "S' ")
    alg = alg.replace("F' B ", "S ")

    alg = alg.replace("B'", "f'")
    alg = alg.replace("B", "f")
    alg = alg.replace("f2", "B2")


    alg = alg.split(" ")

    if alg[-2] == "B'" and alg[-1] == "F":
        del alg[-1]
        alg[-2] == "S'"

    elif alg[-2] == "F'" and alg[-1] == "B":
        del alg[-1]
        alg[-2] == "S"


    for i in range(len(alg)):

        if alg[i] == "S" or alg[i] == "f":
            z_count+=1

        elif alg[i] == "S'" or alg[i] == "f'":
            z_count-=1

        else:
            z_count%=4
            if z_count == 0:
                pass
            
            elif z_count == 1:
                alg[i] = z_dict[alg[i]]

            elif z_count == 2:
                alg[i] = z2_dict[alg[i]]

            else:
                alg[i] = zp_dict[alg[i]]
    a.append(" ".join(alg)+"\n")


move_scores = {
    "R": 1,
    "R'": 1,
    "R2": 3,
    "L": 3,
    "L'": 3,
    "L2": 4,
    "U": 1,
    "U'": 1,
    "U2": 2,
    "D": 2,
    "D'": 2,
    "D2": 4,
    "F": 2,
    "F'": 2,
    "F2": 4,
    "B": 6,
    "B'": 6,
    "B2": 10,
    "f": 2,
    "f'": 2,
    "S": 2,
    "S'": 2
}



rank_list = []
count_list = []
def rank(alg):
    a = alg.strip()
    a = a.split(" ")
    count = 0
    for i in a:
        count += move_scores[i]
    return count


list = []
with open(r"C:\Users\filip\OneDrive - NTNU\Desktop\GitHub\fnilsen1.github.io\Python Projects\tekstfiler\F2_yperm.txt", "r") as file:
    a = file.readlines()
print(a)




liste = []

replacements_y = {'R': 'F', 'L': 'B', 'F': 'L', 'B':'R'}
replacements_y2 = {'R':'L', 'L':'R', 'F': 'B', 'B':'F'}
replacements_yp = {'L':'F', 'R': 'B', 'F':'R', 'B':'L'}

def more(string):
    #y
    copy = string

    replaced_indices = set()
    for old, new in replacements_y.items():
        index = copy.find(old)
        while index != -1:
            if index not in replaced_indices:
                copy = copy[:index] + new + copy[index + len(old):]
                replaced_indices.add(index)
            index = copy.find(old, index + 1)
    a.append(copy)
    copy = string

    replaced_indices = set()
    for old, new in replacements_y2.items():
        index = copy.find(old)
        while index != -1:
            if index not in replaced_indices:
                copy = copy[:index] + new + copy[index + len(old):]
                replaced_indices.add(index)
            index = copy.find(old, index + 1)

    a.append(copy)

    copy = string

    replaced_indices = set()
    for old, new in replacements_yp.items():
        index = copy.find(old)
        while index != -1:
            if index not in replaced_indices:
                copy = copy[:index] + new + copy[index + len(old):]
                replaced_indices.add(index)
            index = copy.find(old, index + 1)

    a.append(copy)

# for i in range(len(a)):
#     # print(i)
#     more(a[i])
    
# for i in range(len(a)):
#     insert_moves(a[i])


print(a)

# # a = set(a)
# # b = a.copy()
# # count = 0
# # for i in range(len(a)):
# #     if a[i].count("2")>4 or a[i].count("B")>0 or a[i].count("L")>0:
# #         del b[i-count]
# #         count+=1

# #     if a[i].count("2")>0:
# #         del b[i-count]
# #         count+=1
    

# dict = {
# 13: 0,
# 14: 0,
# 15: 0,
# 16: 0,
# 17: 0,
# 18: 0

# }

# #Skal funke
# if f"({i})" in a[i]:
#     # print("yes")
#     a[i] = a[i].replace(f" ({i})", "")

# for i in range(len(a)):
#     b = a[i].split(" ")
#     # dict[len(b)]+=1
#     if b[0] == "U2" or b[0] == "U" or b[0] == "U'":
#         del b[0]


#     if b[-1] == "U2\n" or b[-1] == "U\n" or b[-1] == "U'\n":
#         b[-1] = "\n"

        

#     a[i] = " ".join(b)

#     if "(11)" in a[i]:
#         a[i] = a[i].replace(" (11)", "")

#     elif "(12)" in a[i]:
#         a[i] = a[i].replace(" (12)", "")



#     elif "(13)" in a[i]:
#         a[i] = a[i].replace(" (13)", "")

#     elif "(14)" in a[i]:
#         a[i] = a[i].replace(" (14)", "")
#     elif "(15)" in a[i]:
#         a[i] = a[i].replace(" (15)", "")
#     elif "(16)" in a[i]:
#         a[i] = a[i].replace(" (16)", "")

#     elif "(17)" in a[i]:
#         a[i] = a[i].replace(" (17)", "")


#     elif "(18)" in a[i]:
#         a[i] = a[i].replace(" (18)", "")
        
for i in a:
    count_list.append(rank(i))


sorted_values_zip = [v for _, v in sorted(zip(count_list, a))]

with open(r"C:\Users\filip\OneDrive - NTNU\Desktop\GitHub\fnilsen1.github.io\Python Projects\tekstfiler\F2_yperm.txt", "w") as file:
    file.writelines(sorted_values_zip)
        
# for i in range(len(a)):
#     a[i]=a[i].strip()+"\n"


# # a = set(a)
# with open(r"C:\Users\filip\OneDrive - NTNU\Desktop\GitHub\fnilsen1.github.io\Python Projects\tekstfiler\T_zbll_diag.txt", "w") as file:
#     file.writelines(list(a))

