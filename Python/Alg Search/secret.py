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
    print(alg)
    alg = alg.strip()
    z_count = 0

#R2 U2 R' F2 R2 U2 R' B F' U2 B' F' R2 U2 R' F2
    alg = alg.replace("F B'", "S'")
    alg = alg.replace("B F'", "S")
    alg = alg.replace("B' F ", "S'")
    alg = alg.replace("F' B ", "S")

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
                print(alg)
                alg[i] = z_dict[alg[i]]

            elif z_count == 2:
                alg[i] = z2_dict[alg[i]]

            else:
                alg[i] = zp_dict[alg[i]]
    return " ".join(alg)





#Legge til senere
# "B2 F"
# "B2 F'"
# "F B2"
# "F' B2"




