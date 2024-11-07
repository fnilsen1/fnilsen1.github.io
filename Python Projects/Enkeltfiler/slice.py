import copy
import itertools
import sys

"""
Hvilken slice

Ide 1:
input scramble
input skeleton
input dr moveset part

Ide 2:
input type slice
input setup til start slice
input dr sequence

E-slice: FL FR BR BL
M-slice: UF DF DB UB
S-slice: UL UR DR DL (det er en annen option)
"""


#Flere?
slice_combos_3e = ["E E'", "E' E", "E2 E2 E' E", "E2 E' E E2", "E2 E E' E2", "E2 E' E2 E", "E2 E E2 E'", "E' E2 E2 E", "E' E E2 E2", "E' E2 E E2", "E E2 E2 E'", "E E2 E' E2", "E E' E2 E2", "E E2 E E'"]
slice_combos_2e2e = ["E2 E2", "E E E2", "E' E' E2", "E2 E E", "E2 E' E'", "E E2 E", "E' E2 E'"]


slice_dict = {
    
    "R2":[1,2],
    "L2":[0,3],
    "F2":[0,1],
    "B2":[2,3],
    "U2":[[0,1], [0,3]],
    "D2":[[2,3], [2,1]],
    "E":[[0,1],[0,2], [0,3]],
    "E'":[[0,3],[0,2], [0,1]],
    "E2":[[0,2],[1,3]],
    "M":[[0,1],[0,2], [0,3]],
    "M'":[[0,3],[0,2], [0,1]],
    "M2":[[0,2],[1,3]],   
    "S":[[0,1],[0,2], [0,3]],
    "S''":[[0,3],[0,2], [0,1]],
    "S2":[[0,2],[1,3]]
}



def solve_slice(slice_type, insertion_type, setup_start, dr_sequence):
    current_slice = [1,2,3,4]
    
    setup_move_list = setup_start.split()
    print(setup_move_list)

    for k in setup_move_list:
        current_slice = apply_move(slice_type, current_slice, k)

    starting_state = copy.deepcopy(current_slice)

   
    move_list = dr_sequence.split()

    insertion_spots = []
    

    if(insertion_type == "3e"):
        
        if(slice_type == "e"):
            insertion_spots = index_list(move_list, ["U","D"])
            for k in slice_combos_3e:
                insert_slices(len(k.split()), insertion_spots, k, move_list, starting_state, slice_type)


        elif(slice_type == "m"):
            insertion_spots = index_list(move_list, ["R","L"])
            for k in slice_combos_3e:
                insert_slices(len(k.split()), insertion_spots, k.replace("E", "M"), move_list, starting_state, slice_type)
            

        else:
            insertion_spots = index_list(move_list, ["F","B"])
            for k in slice_combos_3e:
                insert_slices(len(k.split()), insertion_spots, k.replace("E", "S"), move_list, starting_state, slice_type)
                   

    else:
        
        if(slice_type == "e"):
            insertion_spots = index_list(move_list, ["U","D"])
            for k in slice_combos_2e2e:
                insert_slices(len(k.split()), insertion_spots, k, move_list, starting_state, slice_type)


        elif(slice_type == "m"):
            
            insertion_spots = index_list(move_list, ["R","L"])
            for k in slice_combos_2e2e:
                insert_slices(len(k.split()), insertion_spots, k.replace("E", "M"), move_list, starting_state, slice_type)
            

        else:
            insertion_spots = index_list(move_list, ["F","B"])
            for k in slice_combos_2e2e:
                insert_slices(len(k.split()), insertion_spots, k.replace("E", "S"), move_list, starting_state, slice_type)
                   


def swap_elements(list, index_1, index_2):
    a = list[index_1]
    list[index_1] = list[index_2]
    list[index_2] = a
    return list

def apply_move(slice_type, current_slice, move):


    if(move not in slice_dict.keys()):
        return current_slice
    
    swap_list = slice_dict[move]

    if((move == "U2" or move == "D2") and slice_type == "e"):
        return current_slice
    
    elif((move == "R2" or move == "L2") and slice_type == "m"):
        return current_slice   

    elif((move == "F2" or move == "B2") and slice_type == "s"):
        return current_slice   

    elif((move == "U2" or move == "D2") and slice_type == "s"):
        swap_list = swap_list[0]

    elif((move == "U2" or move == "D2") and slice_type == "m"):
        swap_list = swap_list[1]

    elif(move[0] == "E" or move[0] == "M" or move[0] == "S"):
        for k in swap_list:
            current_slice = swap_elements(current_slice, k[0], k[1])
        return current_slice
    

    return swap_elements(current_slice, swap_list[0], swap_list[1])

def index_list(move_list, axis_moves):
    insertion_spots = []
    for i in range(len(move_list)):
        if(move_list[i][0]==axis_moves[0] or move_list[i][0]==axis_moves[1]):
            insertion_spots.append(i+1)
    return insertion_spots

def insert_elements_in_list(original_list, index_list, element_list):
    
    tuple_list = list(zip(index_list, element_list))
    sorted_tuple_list = sorted(tuple_list)
    copied_list = copy.deepcopy(original_list)
    for i in range(len(sorted_tuple_list)):
        copied_list.insert(sorted_tuple_list[i][0]+i, sorted_tuple_list[i][1])

    return copied_list

def insert_slices(slice_amount, insertion_spots, insertion_moves, move_list, starting_state, slice_type):
    permutations = set(itertools.combinations(insertion_spots, slice_amount))
    copy_starting_state = tuple(starting_state)
    for k in list(permutations):
        # print("new")
        state = list(copy_starting_state)
        # print("Starting state: ", starting_state)
        # print(insertion_moves.split())

        # print(insert_elements_in_list(move_list, list(k), insertion_moves.split()))
        for v in insert_elements_in_list(move_list, list(k), insertion_moves.split()):
            
            # print(v)
            state = apply_move(slice_type, state, v)
            # print(state)
        # print(" ".join(insert_elements_in_list(move_list, list(k), insertion_moves.split())))
        if(state == [1,2,3,4]):
            print(" ".join(insert_elements_in_list(move_list, list(k), insertion_moves.split())))


def main():
    # a = input("Which slice? [e, m, s] : " )
    # b = input("3e or 2e2e slice? [3e/2e2e]: " )
    # c = input("Setup moves to start slice: ")
    # d = input("Input DR sequence: ")

    # solve_slice(a, b, c)
    # print(swap_elements([1,2,3,4], 0, 3))
    # solve_slice(1,1,1)
    # print(apply_move("e",current_slice, "S"))

    # solve_slice("e", "3e", "R2 B2 R2", "U2 F2 U R2 D' B2 L2 U2 B2 L2 B2")
    # solve_slice("m", "3e", "F2 B2 D2", "L B2 R' B2 R U2 R' U2 F2 R2")
    # solve_slice("m", "3e", "F2 R2", "F2 D' B2 L2 D' B F' U2 F' B' D2")
    # solve_slice("s", "2e2e", "D2", "D2 F2 L2 F' L2 F U2 R2 F2 L2 D2")


    #solve_slice("m", "2e2e", "F2", "L D2 F2 R' D2 R' L2")

    a = input("Which slice? [e, m, s] : " )
    b = input("3e or 2e2e slice? [3e/2e2e]: " )
    c = input("Setup moves to start slice: ")
    d = input("Input DR sequence: ")
    solve_slice(a, b, c, d)

    # solve_slice(a,b,c,d)
    # print(insert_elements_in_list("U2 F2 U R2 D' B2 L2 U2 B2 L2 B2".split(), [1,5], ["E","E'"]))
    # insert_elements_in_list([1], ["e","r","d", "o", "d"],[1,5,3,2,8])

    # insert_elements_in_list([0,0,0,0,0,0,0,0], [3,5,2,1,0], ["e","a", "l", "r", "p"])
 


main()