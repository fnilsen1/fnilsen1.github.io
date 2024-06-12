import json
import time

index_state = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
solved_colors = ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '🟧', '🟧', '🟧', '🟧', '🟧', '🟧', '🟧', '🟧', '🟧', '🟩', '🟩', '🟩', '🟩', '🟩', '🟩', '🟩', '🟩', '🟩', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟨', '🟨', '🟨', '🟨', '🟨', '🟨', '🟨', '🟨', '🟨']
solved = ['h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']
dr_cube = ["d","d","d","d","d","d","d","d","d","x","x","x","x","x","x","x","x","x","x","x","x","r","x","r","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","r","x","r","x","x","x","d","d","d","d","d","d","d","d","d"]
dr_solved = ["d","d","d","d","d","d","d","d","d","x","x","x","x","x","x","x","x","x","x","x","x","r","x","r","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","r","x","r","x","x","x","d","d","d","d","d","d","d","d","d"]
class States():
    def __init__(self, index_state, dr_state, cube_state, total_moves):
        self.index_state = index_state
        self.dr_state = dr_state
        self.cube_state = cube_state
        self.total_moves = total_moves
    

states = States(index_state, dr_cube, solved, 0)
"""
         | 0  1  2  |
         | 3  4  5  |
         | 6  7  8  |

 9 10 11 | 18 19 20 | 27 28 29 | 36 37 38
12 13 14 | 21 22 23 | 30 31 32 | 39 40 41
15 16 17 | 24 25 26 | 33 34 35 | 42 43 44

         | 45 46 47 |
         | 48 49 50 |
         | 51 52 53 |

"""

move_dict = {
"U":[6, 3, 0, 7, 4, 1, 8, 5, 2, 18, 19, 20, 12, 13, 14, 15, 16, 17, 27, 28, 29, 21, 22, 23, 24, 25, 26, 36, 37, 38, 30, 31, 32, 33, 34, 35, 9, 10, 11, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53],
"U'":[2, 5, 8, 1, 4, 7, 0, 3, 6, 36, 37, 38, 12, 13, 14, 15, 16, 17, 9, 10, 11, 21, 22, 23, 24, 25, 26, 18, 19, 20, 30, 31, 32, 33, 34, 35, 27, 28, 29, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53],
"U2":[8, 7, 6, 5, 4, 3, 2, 1, 0, 27, 28, 29, 12, 13, 14, 15, 16, 17, 36, 37, 38, 21, 22, 23, 24, 25, 26, 9, 10, 11, 30, 31, 32, 33, 34, 35, 18, 19, 20, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53],
"R":[0, 1, 20, 3, 4, 23, 6, 7, 26, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 47, 21, 22, 50, 24, 25, 53, 33, 30, 27, 34, 31, 28, 35, 32, 29, 8, 37, 38, 5, 40, 41, 2, 43, 44, 45, 46, 42, 48, 49, 39, 51, 52, 36],
"R'":[0, 1, 42, 3, 4, 39, 6, 7, 36, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 21, 22, 5, 24, 25, 8, 29, 32, 35, 28, 31, 34, 27, 30, 33, 53, 37, 38, 50, 40, 41, 47, 43, 44, 45, 46, 20, 48, 49, 23, 51, 52, 26],
"R2":[0, 1, 47, 3, 4, 50, 6, 7, 53, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 42, 21, 22, 39, 24, 25, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 37, 38, 23, 40, 41, 20, 43, 44, 45, 46, 2, 48, 49, 5, 51, 52, 8],
"F":[0, 1, 2, 3, 4, 5, 17, 14, 11, 9, 10, 45, 12, 13, 46, 15, 16, 47, 24, 21, 18, 25, 22, 19, 26, 23, 20, 6, 28, 29, 7, 31, 32, 8, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 33, 30, 27, 48, 49, 50, 51, 52, 53],
"F'":[0, 1, 2, 3, 4, 5, 27, 30, 33, 9, 10, 8, 12, 13, 7, 15, 16, 6, 20, 23, 26, 19, 22, 25, 18, 21, 24, 47, 28, 29, 46, 31, 32, 45, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 11, 14, 17, 48, 49, 50, 51, 52, 53],
"F2":[0, 1, 2, 3, 4, 5, 47, 46, 45, 9, 10, 33, 12, 13, 30, 15, 16, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 28, 29, 14, 31, 32, 11, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 8, 7, 6, 48, 49, 50, 51, 52, 53],
"D":[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 42, 43, 44, 18, 19, 20, 21, 22, 23, 15, 16, 17, 27, 28, 29, 30, 31, 32, 24, 25, 26, 36, 37, 38, 39, 40, 41, 33, 34, 35, 51, 48, 45, 52, 49, 46, 53, 50, 47],
"D'":[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 24, 25, 26, 18, 19, 20, 21, 22, 23, 33, 34, 35, 27, 28, 29, 30, 31, 32, 42, 43, 44, 36, 37, 38, 39, 40, 41, 15, 16, 17, 47, 50, 53, 46, 49, 52, 45, 48, 51],
"D2":[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 33, 34, 35, 18, 19, 20, 21, 22, 23, 42, 43, 44, 27, 28, 29, 30, 31, 32, 15, 16, 17, 36, 37, 38, 39, 40, 41, 24, 25, 26, 53, 52, 51, 50, 49, 48, 47, 46, 45],
"L":[44, 1, 2, 41, 4, 5, 38, 7, 8, 15, 12, 9, 16, 13, 10, 17, 14, 11, 0, 19, 20, 3, 22, 23, 6, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 51, 39, 40, 48, 42, 43, 45, 18, 46, 47, 21, 49, 50, 24, 52, 53],
"L'":[18, 1, 2, 21, 4, 5, 24, 7, 8, 11, 14, 17, 10, 13, 16, 9, 12, 15, 45, 19, 20, 48, 22, 23, 51, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 6, 39, 40, 3, 42, 43, 0, 44, 46, 47, 41, 49, 50, 38, 52, 53],
"L2": [45, 1, 2, 48, 4, 5, 51, 7, 8, 17, 16, 15, 14, 13, 12, 11, 10, 9, 44, 19, 20, 41, 22, 23, 38, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 24, 39, 40, 21, 42, 43, 18, 0, 46, 47, 3, 49, 50, 6, 52, 53],
"B":[29, 32, 35, 3, 4, 5, 6, 7, 8, 2, 10, 11, 1, 13, 14, 0, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 53, 30, 31, 52, 33, 34, 51, 42, 39, 36, 43, 40, 37, 44, 41, 38, 45, 46, 47, 48, 49, 50, 9, 12, 15],
"B'":[15, 12, 9, 3, 4, 5, 6, 7, 8, 51, 10, 11, 52, 13, 14, 53, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 30, 31, 1, 33, 34, 2, 38, 41, 44, 37, 40, 43, 36, 39, 42, 45, 46, 47, 48, 49, 50, 35, 32, 29],
"B2":[53, 52, 51, 3, 4, 5, 6, 7, 8, 35, 10, 11, 32, 13, 14, 29, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 15, 30, 31, 12, 33, 34, 9, 44, 43, 42, 41, 40, 39, 38, 37, 36, 45, 46, 47, 48, 49, 50, 2, 1, 0]
}
def define_move(cycle_list):
    snapshot = index_state.copy()
    for i in range(len(cycle_list)):
        for j in range(len(cycle_list[i])):
            index_state[cycle_list[i][j]]=snapshot[cycle_list[i][j-1]]

# define_move([[37,41,43,39],[36,38,44,42],[53,29,0,15],[52,32,1,12],[51,35,2,9]])

#U: [[0,2,8,6],[1,5,7,3],[19,10,37,28],[11,38,29,20],[9,36,27,18]]
#R: [[27,29,35,33],[28,32,34,30],[47,20,2,42],[50,23,5,39],[53,26,8,36]]
#F: [[18,20,26,24],[19,23,25,21],[7,30,46,14],[6,27,47,17],[8,33,45,11]]
#D: [[46,50,52,48],[45,47,53,51],[25,34,43,16],[24,33,42,15],[17,26,35,44]]
#L: [[3,21,48,41],[10,14,16,12],[9,11,17,15],[0,18,45,44],[6,24,51,38]]
#B: [[37,41,43,39],[36,38,44,42],[53,29,0,15],[52,32,1,12],[51,35,2,9]]


def apply_transformation(transformation):
    dr_copy = states.dr_state.copy()
    cube_copy = states.cube_state.copy()
    
    for i in range(len(states.cube_state)):
        if(i!=transformation[i]):
            states.cube_state[i]=cube_copy[transformation[i]]
            states.dr_state[i]=dr_copy[transformation[i]]


def apply_alg(alg):
    alg = alg.split(" ")
    for i in alg:
        apply_transformation(move_dict[i])


# apply_alg("L D2 R2 D U2 L2 U' F2 U' R2 U' R F L' D B' U R2 F D'")

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

    file_path = 'Python\Kociemba\\dr7movers.txt'
   
    with open(file_path, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            line = line.strip()
            states.cube_state=solved.copy()
            apply_alg(inverse(line))

            if ''.join(states.cube_state) not in obj:
                obj[''.join(states.cube_state)]=line

    # Close the file
    file.close()

    filnavn = "Python\Kociemba\\phase2_lookup_moveset.json"
    with open(filnavn, "w") as fil:
        fil.write(json.dumps(obj, indent = 2))





# lookup()

def solve_dr(scramble):
    t = time.time()
    file_path = 'Python Projects\Kociemba\\1_6movers.txt'
    with open('Python Projects\Kociemba\\DR_lookup.json') as file:
        data = json.load(file)
        
    states.dr_state=dr_solved.copy()
    apply_alg(scramble) 

    if ''.join(states.dr_state) in data:
        print(data[''.join(states.dr_state)])
        x = data[''.join(states.dr_state)].split()
        states.total_moves+=len(x)
        apply_alg(data[''.join(states.dr_state)])
        
        solve()
    else:

        with open(file_path, 'r') as file:
            # Iterate over each line in the file
            for line in file:
                line = line.strip()
                apply_alg(line)
                if ''.join(states.dr_state) in data:
                    print(line+" "+data[''.join(states.dr_state)])
                    x = (line+" "+data[''.join(states.dr_state)]).split()
                    states.total_moves+=len(x)

                    apply_alg(data[''.join(states.dr_state)])
                    solve()
                    return
                else:
                    apply_alg(inverse(line))

        file.close()

def solve():
    file_path = 'Python Projects\Kociemba\\dr7movers.txt'
    with open('Python Projects\Kociemba\phase2_lookup_moveset.json') as file:
        data = json.load(file)
        
    states.cube_state=states.cube_state.copy()

    # apply_alg(scramble) 

    if ''.join(states.cube_state) in data:
        print(data[''.join(states.cube_state)])
        x = data[''.join(states.cube_state)].split()
        states.total_moves+=len(x)
        print(states.total_moves)
    else:

        with open(file_path, 'r') as file:
            # Iterate over each line in the file
            for line in file:
                line = line.strip()
                apply_alg(line)
                if ''.join(states.cube_state) in data:
                    print(line+" "+data[''.join(states.cube_state)])
                    x = (line+" "+data[''.join(states.cube_state)]).split()
                    states.total_moves+=len(x)
                    print(states.total_moves)                    
                    return
                else:
                    apply_alg(inverse(line))

        file.close()

#Sett inn scrambelen her bois
# scramble_list = [
# "F2 B2 U' L D2 L2 F' B L F R2 F L2 F2 U2 R2 U2 B' D2", 
# "R D2 L B2 L2 B2 U2 L' F2 R U2 R' B' L' D L' B' D2 B2 D L'", 
# "U2 D' L' U' D2 R2 B' U F2 R2 F2 L2 D2 L' U2 D2 F2 L' F", 
# "B' F2 D' B2 U R2 F2 U L2 R2 B2 R2 U' L' B D' B2 F' L2 D L2", 
# "B' L2 D2 L2 R2 B' R2 F U2 R2 L U' B' D' F' D' U' B' L" 
# ]r

# scramble_list = [
# "F2 B2 U' L D2 L2", 
# "R D2 L B2 L2 B2", 

# ]

# def solve_scrambles(list):
# index_copy = index_state.copy()

# dr_copy = dr_cube.copy()
# solved_copy = solved.copy()

# for i in range(len(scramble_list)):

#     # states = States(index_copy, dr_copy, solved_copy, 0)
#     states.index_state = index_copy
#     states.dr_state = dr_copy
#     states.solved = solved_copy
#     states.total_moves = 0
#     print(states.dr_state)
#     print(states.solved)

#     solve_dr(scramble_list[i])

# solve_scrambles(scramble_list)
solve_dr("F2 U' F' R2 U F2 L2 D2 R L2 B' D2 B' U2 D2 B2 R2 U2 F'")



# Python Projects\Kociemba\DR_lookup.json
