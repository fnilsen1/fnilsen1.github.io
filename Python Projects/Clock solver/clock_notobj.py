import numpy as np
import random

"""
Representation
[0,1,2,3,4,5,6,7,8,9,10,11,12,13]

0  1  2        9
3  4  5    10 11 12
6  7  8       13

The back side is a y-rotation away from the front side
Front:       Back:
|0 11  0|    |1  10 10|
|0  0  0|    |3  11  3|
|10 0  1|    |2   5  0|  

Pins
[1, -1, -1, 1]
Indicies
    0  1
    2  3
"""

"""
Moves
UR
DR
DL
UL
U
R
D
L
All


0  1  2        9
3  4  5    10 11 12
6  7  8       13
"""
state = np.zeros(14, dtype=int)

front_sets = {
'UL':[0,1,3,4], 'UR':[1,2,4,5], 'DL':[3,4,6,7], 'DR':[4,5,7,8],
'R':[1,2,4,5,7,8], 'L':[0,1,3,4,6,7],'D':[3,4,5,6,7,8],'U':[0,1,2,3,4,5],'ALL':[0,1,2,3,4,5,6,7,8]
}
               
back_sets = {
'UL':[2,9,10,11],'UR':[0,9,11,12],'DL':[8,10,11,13], 'DR':[6,11,12,13],
'R':[0,6,9,11,12,13],'L':[2,8,9,10,11,13],'D':[6,8,10,11,12,13],'U':[0,2,9,10,11,12],'ALL':[0,2,6,8,9,10,11,12,13]
}
#Length of string : amount of corners in list
corner_amount = {1:2, 2:1, 3:4}

def apply_move(state, move, side='front'):
    move_type, turns = move[0:len(move)-2], int(move[-1]+move[-2])

    if side=='front':
        for k in (front_sets[move_type]):
            state[k]+=turns
    else:
        for i in range(corner_amount[len(move_type)]):
            state[back_sets[move_type][i]]-=turns

        for i in range(corner_amount[len(move_type)], len(back_sets[move_type])):
            state[back_sets[move_type][i]]+=turns

    return state%12

def apply_alg(alg, state):
    alg = alg.split(" y2 ")
    front_part = alg[0].split(" ")
    back_part = alg[1].split(" ")       

    for k in front_part:
        state = apply_move(state, k)

    for k in back_part:
        state = apply_move(state, k, "back")

    return state

def print_state(state):
    print("".join(f"{num:<{4}}" for num in state[0:3]), end="|  ")
    print("".join(f"{num:<{4}}" for num in [-1*state[2]%12,state[9],-1*state[0]%12]))

    print("".join(f"{num:<{4}}" for num in state[3:6]), end="|  ")
    print("".join(f"{num:<{4}}" for num in state[10:13]))

    print("".join(f"{num:<{4}}" for num in state[6:9]), end="|  ")
    print("".join(f"{num:<{4}}" for num in [-1*state[8]%12,state[13],-1*state[6]%12]))


# state = apply_move(state, 'UR5+')
# state = apply_move(state, 'ALL1+')
move_list = ['UR','UL','DR','DL','R','L','U','D','ALL']
scramble_moves = [move_list[random.randint(0,6)]]


state = apply_alg("UR1+ DR1+ DL6+ UL4+ U5- R5+ D6+ L2- ALL5+ y2 U2+ R1- D2- L4- ALL5+", state)
temp = ""
for k in state:
    temp+=str(k)+" "
print(temp)
# print_state(state)







