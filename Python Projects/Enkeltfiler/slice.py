import copy
import itertools

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
    "S'":[[0,3],[0,2], [0,1]],
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
            print("yes")
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
    # print(permutations)
    copy_starting_state = tuple(starting_state)

    for k in list(permutations):
        # print("new")
        state = list(copy_starting_state)
        # print("Starting state: ", starting_state)
        # print(insertion_moves.split())

        # print(insert_elements_in_list(move_list, list(k), insertion_moves.split()))
        # print(" ".join(insert_elements_in_list(move_list, list(k), insertion_moves.split())))
        for v in insert_elements_in_list(move_list, list(k), insertion_moves.split()):
            
            # print(v)
            state = apply_move(slice_type, state, v)
            # print(state)
        
        # print(state)
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
    solve_slice("s", "2e2e", "D2 R2", "U2 F L2 F' U2 F R2 D2 B2 R2 D2 L2 F2")


    # solve_slice(a,b,c,d)  
    # print(insert_elements_in_list("U2 F2 U R2 D' B2 L2 U2 B2 L2 B2".split(), [1,5], ["E","E'"]))
    # insert_elements_in_list([1], ["e","r","d", "o", "d"],[1,5,3,2,8])

    # insert_elements_in_list([0,0,0,0,0,0,0,0], [3,5,2,1,0], ["e","a", "l", "r", "p"])
 


main()

#Add klassen tilbake
# def searchInsert(nums, target):

#     middle_index = round(len(nums)/2)-1
#     id = middle_index
#     while len(nums)>2:

#         if(nums[middle_index]>=target):
 
#             nums = nums[:middle_index+1]
#             print(nums)
#             middle_index = round(len(nums)/2)-1
#             id-=middle_index-1

#         else:
#             print("ayooo")
#             nums = nums[middle_index+1:]
#             print(nums)
#             middle_index = round(len(nums)/2)-1
#             print(middle_index)
#             id+=middle_index+1

#     if(nums[0]==target):
#         return id
    
#     else:
#         return id+1

# print(searchInsert([1,3,5,6], 4))

#burde ha egen liste med indekser
    
# class Solution(object):
#     def maximumSubarraySum(self, nums, k):
#         ordbok = {}
#         maximum = float("-inf")
#         no_good = True
#         for i in range(len(nums)):
#             if nums[i] in ordbok:
#                 no_good = False
#                 for j in ordbok[nums[i]]:
#                     maximum = max(maximum, sum(nums[j: i+1]))

#             if nums[i]+k not in ordbok:
#                 ordbok[nums[i]+k] = []

#             if nums[i]-k not in ordbok:
#                 ordbok[nums[i]-k] = []

#             if nums[i]+k in ordbok:
#                 ordbok[nums[i]+k].append(i)

#             if nums[i]-k in ordbok:
#                 ordbok[nums[i]-k].append(i)

#         if no_good:
#             return 0
#         else:
#             print(maximum)

# # [1,2,3,4,5]
# solution = Solution()

# nums= [4,7,3,5,5]
# # nums = [-636,-784,-356,-832,-797,-978,-651,-667,-907,-900,-168,-697,-879,-998,-126,-900,-542,-553,-268,-374,-710,-768,-727,-975,-106,-756,-462,-815,-276,-163,-301,-822,-367,-685,-581,-488,-763,-612,-847,-730,-479,-874,-221,-912,-229,-543,-876,-845,-424,-215,-819,-164,-840,-525,-987,-291,-658,-168,-382,-781,-951,-396,-228,-394,-445,-863,-290,-675,-289,-950,-885,-228,-624,-236,-437,-246,-302,-741,-243,-419,-851,-980,-667,-661,-140,-893,-328,-354,-359,-845,-396,-309,-450,-941,-310,-119,-614,-854,-599,-605]
# solution.maximumSubarraySum(nums, 2)
# for i in range(len(nums)-1):
#     for j in range(1+i, len(nums)):   
#         if(abs(nums[j]-nums[i])==8):
#             print(i, " : ", nums[i]," ", j, " : ", nums[j])
#             print(sum(nums[i:j+1]))

#[-1, 3, 2]
#[2,4,5]





#Timed out
# class Solution(object):
#     def maximumSubarraySum(self, nums, k):
#         ordbok = {}
#         maximum = float("-inf")
#         no_good = True
#         for i in range(len(nums)):
#             if nums[i] in ordbok:
#                 no_good = False
#                 for j in ordbok[nums[i]]:
#                     maximum = max(maximum, sum(nums[j: i+1]))

#             if nums[i]+k not in ordbok:
#                 ordbok[nums[i]+k] = []

#             if nums[i]-k not in ordbok:
#                 ordbok[nums[i]-k] = []

#             if nums[i]+k in ordbok:
#                 ordbok[nums[i]+k].append(i)

#             if nums[i]-k in ordbok:
#                 ordbok[nums[i]-k].append(i)

#         if no_good:
#             return 0
#         else:
#             return maximum


# class Solution(object):
#     def maximumSubarraySum(self, nums, k):
#         ordbok = {}
#         maximum = float("-inf")
#         no_good = True
#         for i in range(len(nums)):
#             if nums[i]-k in ordbok:
#                 no_good = False
#                 for j in ordbok[nums[i]-k]:
#                     maximum = max(maximum, sum(nums[j: i+1]))

#             if nums[i]+k in ordbok:
#                 no_good = False
#                 for v in ordbok[nums[i]+k]:
#                     maximum = max(maximum, sum(nums[v: i+1]))

#             if nums[i] not in ordbok:
#                 ordbok[nums[i]] = []

#             if nums[i] in ordbok:
#                 ordbok[nums[i]].append(i)

#         if no_good:
#             return 0
#         else:
#             return maximum


# class Solution:
#     def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
#         if (a==e or b==f) and not (((c==a) and ((d>b and d<f) or (d>f and d<b))) or ((d==b) and ((c>a and c<e) or (c>e and c<a)))):
#             return 1

#         elif abs(c-e) == abs(d-f) and not (abs(a-c) == abs(b-d) and ((a>e and a<c) or (a>c and a<e))):
#             return 1

#         else:
#             return 2

