# import json
# class Globals():
#     def __init__(self, start_list, index_list, all_algs):
#         self.start_list = start_list
#         self.index_list = index_list
#         self.all_algs = all_algs

# globals = Globals([],[],[])
# moves = ["R","R'","R2","L","L'","L2","U","U'","U2","D","D'","D2","F","F'","F2","B","B'","B2"]

# def gen(length):
#     for i in range(length):
#         globals.index_list[i]+=1
#         globals.index_list[i]%=18
#         if globals.index_list[i]:
#             break

#     for i in range(length-1):
#         if globals.index_list[i]//3==globals.index_list[i+1]//3:
#             pass
#         elif globals.index_list[i]//6==globals.index_list[i+1]//6 and (globals.index_list[i]//3)%2:
#             pass
#     for i in range(length-2):
#         if globals.index_list[i]//6==globals.index_list[i+1]//6 and globals.index_list[i]//3==globals.index_list[i+2]//3:
#             pass
    
#     move_list = globals.index_list.copy()
#     for i in range(length):
#         move_list[i]=moves[move_list[i]]

#     return " ".join(move_list)
#     # globals.all_algs.append(" ".join(move_list))

# def gen_algs(n):
#     file_path = 'Python\Kociemba\\dr7movers.txt'

#     # Open the file in append mode
#     with open(file_path, 'a') as file:
#         # Write the new line to the file

#         for i in range(1,n+1):
#             globals.index_list = [17]*i
#             globals.starting_list = globals.index_list.copy()
#             file.write(gen(i) + '\n')
#             while globals.index_list!=globals.starting_list:
#                 file.write(gen(i) + '\n')
            

                

#         # Close the file
#     file.close()

            
#     # obj={"algs":globals.all_algs}
#     # filnavn = "Python\Kociemba\\7algs.json"
#     # with open(filnavn, "w") as fil:
#     #     fil.write(json.dumps(obj, indent = 2))

# gen_algs(6)


import json
class Globals():
    def __init__(self, start_list, index_list, all_algs):
        self.start_list = start_list
        self.index_list = index_list
        self.all_algs = all_algs

globals = Globals([],[],[])
moves = ["U","U'","U2","D","D'","D2","F2","B2","R2","L2",]

def gen(length):
    for i in range(length):
        globals.index_list[i]+=1
        globals.index_list[i]%=10
        if globals.index_list[i]:
            break

    for i in range(length-1):
        if globals.index_list[i]//3==globals.index_list[i+1]//3 and globals.index_list[i]<6:
            pass
        elif globals.index_list[i]//6==globals.index_list[i+1]//6 and (globals.index_list[i]//3)%2 and globals.index_list[i]<6:
            pass

    
    move_list = globals.index_list.copy()

    for i in range(length):
        move_list[i]=moves[move_list[i]]
  
    return " ".join(move_list)


def gen_algs(n):
    file_path = 'Python\Kociemba\\dr7movers.txt'
    with open(file_path, 'a') as file:
        for i in range(1,n+1):
            globals.index_list = [9]*i
            globals.starting_list = globals.index_list.copy()
            file.write(gen(i) + '\n')
            while globals.index_list!=globals.starting_list:
                file.write(gen(i) + '\n')
    file.close()

gen_algs(7)


