import alg_list
import scrambles
import json
import time
index_state = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
# cube_state = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
# solved = ['⬜', '⬜️', '⬜️', '⬜️', '🟧', '🟧', '🟧', '🟧', '🟩', '🟩', '🟩', '🟩', '🟥', '🟥', '🟥', '🟥', '🟦', '🟦', '🟦', '🟦', '🟨', '🟨', '🟨', '🟨']
# solved = ["a","a","a","a","b","b","b","b","c","c","c","c","d","d","d","d","e","e","e","e","f","f","f","f"]
solved = ["h","h","h","h","o","o","o","o","g","g","g","g","r","r","r","r","b","b","b","b","G","G","G","G"]

class States():
    def __init__(self, index_state, cube_state):
        self.index_state = index_state
        self.cube_state = cube_state

states = States(index_state, solved)
"""
       | 0 1 |
       | 2 3 |

| 4 5  | 8 9 | 12 13 | 16 17 |
| 6 7  |10 11| 14 15 | 18 19 |

       |20 21|
       |22 23|

"""


move_dict = {

"R":[0, 9, 2, 11, 4, 5, 6, 7, 8, 21, 10, 23, 14, 12, 15, 13, 3, 17, 1, 19, 20, 18, 22, 16],
"R'":[0, 18, 2, 16, 4, 5, 6, 7, 8, 1, 10, 3, 13, 15, 12, 14, 23, 17, 21, 19, 20, 9, 22, 11],
"R2":[0, 21, 2, 23, 4, 5, 6, 7, 8, 18, 10, 16, 15, 14, 13, 12, 11, 17, 9, 19, 20, 1, 22, 3],
"U":[2, 0, 3, 1, 8, 9, 6, 7, 12, 13, 10, 11, 16, 17, 14, 15, 4, 5, 18, 19, 20, 21, 22, 23],
"U'":[1, 3, 0, 2, 16, 17, 6, 7, 4, 5, 10, 11, 8, 9, 14, 15, 12, 13, 18, 19, 20, 21, 22, 23],
"U2":[3, 2, 1, 0, 12, 13, 6, 7, 16, 17, 10, 11, 4, 5, 14, 15, 8, 9, 18, 19, 20, 21, 22, 23],
"F":[0, 1, 7, 5, 4, 20, 6, 21, 10, 8, 11, 9, 2, 13, 3, 15, 16, 17, 18, 19, 14, 12, 22, 23],
"F'":[0, 1, 12, 14, 4, 3, 6, 2, 9, 11, 8, 10, 21, 13, 20, 15, 16, 17, 18, 19, 5, 7, 22, 23],
"F2":[0, 1, 21, 20, 4, 14, 6, 12, 11, 10, 9, 8, 7, 13, 5, 15, 16, 17, 18, 19, 3, 2, 22, 23],


}
#"B":[13, 15, 2, 3, 1, 5, 0, 7, 8, 9, 10, 11, 12, 23, 14, 22, 18, 16, 19, 17, 20, 21, 4, 6]

def define_move(cycle_list):
    snapshot = index_state.copy()
    for i in range(len(cycle_list)):
        for j in range(len(cycle_list[i])):
            index_state[cycle_list[i][j]]=snapshot[cycle_list[i][j-1]]

    print(index_state)

# define_move([[3,14,20,5], [9,11,10,8],[2,12,21,7]])


def apply_transformation(transformation):
    cube_copy = states.cube_state.copy()
    for i in range(len(states.cube_state)):
        if(i!=transformation[i]):
            states.cube_state[i]=cube_copy[transformation[i]]


def apply_alg(alg):
    alg = alg.split(" ")
    for i in alg:
        apply_transformation(move_dict[i])
  

# apply_alg("F2 U R2 U F U2 R' U' R'")

def inverse(alg):
    alg = alg.split(" ")
    alg.reverse()
    for i in range (len(alg)):
        if(len(alg[i])==2):
            alg[i]=alg[i].replace("'", "")
        else:
            alg[i]+="'"
    return " ".join(alg)

# print(inverse("R U"))

def lookup():
    obj = {}

    for i in range(len(alg_list.alg_list)):
        states.cube_state=solved.copy()
        apply_alg(inverse(alg_list.alg_list[i]))

        if ''.join(states.cube_state) not in obj:
            obj[''.join(states.cube_state)]=alg_list.alg_list[i]


    filnavn = "algs.json"
    with open(filnavn, "w") as fil:
        fil.write(json.dumps(obj, indent = 2))

# lookup()
<<<<<<< HEAD:Python Projects/Solver/2x2.py
with open('algs.json') as file:
=======
with open("algs.json") as file:
>>>>>>> 910fda8dffe3fbfa06c75c4ceab48e5bd5909afd:Python Projects/Solver/twobytwo_solver.py
    data = json.load(file)
    
def solve(scramble):
    states.cube_state=solved.copy()
    apply_alg(scramble) 
    if ''.join(states.cube_state) in data:
        print(data[''.join(states.cube_state)])
    else:
        for i in range(len(alg_list.alg_list)):
            apply_alg(alg_list.alg_list[i])
            if ''.join(states.cube_state) in data:
                print(alg_list.alg_list[i]+" "+data[''.join(states.cube_state)])
                return
            else:
                apply_alg(inverse(alg_list.alg_list[i]))


if __name__ == "__main__":
    solve("R U R'")

# for i in range(10000):
#     solve(scrambles.scrambles[i])

# end_time = time.time()
# elapsed_time = end_time - start_time
# print(elapsed_time)

