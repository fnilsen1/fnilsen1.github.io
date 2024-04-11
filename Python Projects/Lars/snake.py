# # import numpy as np
# # # liste = ["B D' L' B' R2 L2 B' U F2 D2 U2 R U F U' L2 F U'", "F2 B2 U2 D' F' U2 R2 F B R' U' L B2 L' U L2 U' D2", "F2 U R2 U D B L2 U2 F2 D2 R' D2 U' R U' R2 U' F U2", "U2 D2 F2 B2 D F' U2 R2 F B R' U' L B2 L' U L2 U' D2", "U D2 B' R2 D' F D L U R2 F2 D R2 U' L U' L U F'", "L U L2 D' L' D' L B' D' F2 R2 F2 B R2 L D B2 R' D2", "F2 U2 D2 F2 D F D2 F B L' D2 B2 U L B2 L' D F2 D", "D' L B L' F2 D L2 D' B2 L' D' L U2 F' D F' U' B2 D", "B2 U2 D2 B2 D F D2 F B L' D2 B2 U L B2 L' D F2 D", "D' L2 B' L2 B2 U L F' R2 U R2 U B U F' R2 U F2 D", "D L2 B' R F B' L2 D' B2 R U B' L2 F' B' D' B2 L2 B2", "D2 R2 F2 B2 D' B L2 U' B R2 U' F2 B2 D' R U2 D' L2 U2", "L2 U2 F2 U F L U B2 U' D' R D F' R2 D F' D2 U2 B'", "U2 L F' L' B2 L F B' D R' D B2 L' D' U' B' D' L' R'", "D' F2 D F2 B' D2 B' U D F2 U F2 B R2 F2 L' B2 U' F2", "U2 L B' D2 B2 R U2 R' U' L F2 U' L2 D2 B2 U2 B' U L'", "D2 R' U' B' R L' D' L' U' B2 R2 U' L' B2 F2 U2 R D2 R'", "D2 R' U' B' R L' D' L' U' B2 R2 U' R' D2 U2 F2 R B2 L'", "B U2 B L' U' F2 D R2 B2 L F' U2 F' R' F B2 L U R2", "U2 F R2 L2 B D L D2 B D' F' U B' R U R' F2 D2 F2", "D B L U2 F B U R2 F' L' R2 U2 B F' R F R2 D' B", "B2 U' L U2 F' U' B R' U2 D' R F2 D L U F' D R L2", "F2 U' F2 U2 B R2 F' B' R U R2 B F R' F' U2 F2 L' F'", "D B' U B R' F2 R' D2 B D' L' D R2 L2 F' D2 L B D", "B U' L D' R U R' D' B L2 U' R F2 D2 U2 B2 R' U' R", "B U' L D' R U R' D' B L2 U' R B2 U2 D2 F2 R' U' R", "D B' L2 D R L2 F D' R F' R2 U R2 U B' U2 B' D U", "B U' F' U R2 U' L' U D' R2 D' B U' D' B2 R F' U2 L2", "L' D2 L2 D2 F R2 F' D L2 F U' L R' D2 U' F2 L B' D", "B D2 R2 U' D L U' B L F U' L2 U2 F2 D' B' U' D2 F2", "B' D B' D L U' B' R B2 F2 L U2 F L2 F L R D2 F'", "B D2 L D R2 F2 U2 F U F' D B2 R' U2 F' L' F2 L F", "L' D' B2 L2 U' R2 B U2 L' D' B' L' D B2 U2 L' B R' F2", "L' F U D' L B2 L F2 U' R F2 U R2 F2 U' R D L' B", "L2 F U2 D2 L2 F2 R' B L B' U2 L2 F' R F U L B' F", "L2 F U2 L2 F2 R' B L B' U2 L2 F' B2 R F U L B' F", "B D' L' B' R2 L2 B U2 D2 F2 U B2 R U F U' L2 F U'", "R F D2 L2 F2 R' F' R2 F2 R D' B' R B D' F' L' U B'", "L2 F D' B U B' L' U2 R' L' D B' U' B R2 U2 R B D2", "R F2 D F B L U' R L' U2 L' U L' U' R2 U2 F' U F2", "R2 L' D' F2 R U D2 F2 L' F R D U' L R2 B' D B' U'", "B2 R2 D' B D B' U L B' L2 D' B L B D R2 B' U R2", "L2 F2 R B' U' D B' L U' R L D B L F' L2 U2 F2 B'", "B R2 D R' B2 R U2 F B2 L D2 R2 D' R' D2 L' R' F' D'", "L2 F' R' D L2 D2 B' R' U2 B R2 U R2 F' R' U2 R F D'", "B2 L2 U F' L2 D R2 F B2 D2 R2 F L' U' F2 D B2 D' R", "R' B' U' R U D2 R F' L2 D2 B' D2 L' F2 U B' U L' R'", "F2 B2 U2 L' D' F' L2 F' L' B' L' U2 F' R' F2 U2 L2 R2 U", "U' B R F2 R B' D R' D' L F' L2 R' B' L R2 B L' F'", "F B' R U' R2 L2 F' B L2 B U L' F2 D' L' B2 L' U' F", "F2 B' U' B2 D2 B2 L2 U2 F U2 R' F D' U2 F' U' R2 F U'", "F2 B' D' B' D2 F' B2 U2 B L U R U' D2 L B' D2 R2 U", "F2 B' R' B2 R2 B D R2 U2 B' L' F R B2 L' U' D2 F2 U2"]
# # liste = []
# # with open(r'fnilsen1.github.io\Python\Lars\best_solutions (1).txt') as topo_file:
# #     for line in topo_file:
# #         liste.append(line.strip())  # The comma to suppress the extra new line char

# # # print(liste)
# # my_dict = {}
# # #[B moves, L moves, Double moves]
# # for i in range(len(liste)):
# #     my_dict[liste[i]] = [0, 0, 0]
# #     for j in liste[i]:
# #         if j == "B":
# #             my_dict[liste[i]][0]+=1

# #         if j == "L":
# #             my_dict[liste[i]][1]+=1

# #         elif j == "2":
# #             my_dict[liste[i]][2]+=1
# # sorted_tuples = sorted(my_dict.items(), key=lambda x: x[1][0])
# # sorted_dict = dict(sorted_tuples)


# # sums = []
# # for i, j in sorted_dict.items():
# #     sum = 0
# #     b = j[0]
# #     for k in j:
# #         sum+=k
# #     sums.append(sum)
# #     print(i, j, f"B: {b}", f"Sum: {sum}")

# # # print(sums)
# # # solutions = list(my_dict.keys())
# # # combined_lists = list(zip(solutions, sums))

# # # # Sort based on the values from the second list (list2)
# # # sorted_combined_lists = sorted(combined_lists, key=lambda x: x[1])

# # # # Extract the sorted elements back into separate lists
# # # sorted_list1, sorted_list2 = zip(*sorted_combined_lists)


# # # for i in range(len(sorted_list1)):
# # #     print(sorted_list1[i], sorted_list2[i])

# import math
# def is_prime(n):

#     if n==1 or int(n)==2:
#         return True

#     for i in range(2, math.ceil(math.sqrt(n))):
#         if(n%i ==0):
#             return False
    
#     # print(n)
#     return True


# def is_sdp(n):
#     sum = 0
#     for i in str(n):
#         sum+=int(i)

#     if((n/sum)%2==0 or (n/sum)%1!=0 or (n/sum)==1.0):
#         return False

#     if(is_prime(n/sum)):
#         print(n/sum)
#         return True

#     return False

# svar = 0
# for i in range(1, 101):
#     svar+=is_sdp(i)


# print(svar)
# # print(is_prime(1.1))



# #finn ut av split

a = [1,2,3]
a.reverse()
print(a)