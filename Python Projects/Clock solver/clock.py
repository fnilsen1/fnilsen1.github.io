import numpy as np
#vurder sets mellom klokkegrupper for representasjon

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


class Clock:
    def __init__(self, state, pins):
        self.state = state 
        self.pins = pins

class Small_clock:
    def __init__(self, value, move_list):
        self.value = value
        self.move_list = move_list
        # self.pin_list = pin_list
        

def print_clock(state):
    pass
"""

Front:       Back:
|0 11  0|    |1  10 10|
|0  0  0|    |3  11  3|
|10 0  1|    |2   5  0|  

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
"""
move_lists = [
['UL','L','U','ALL'],
['UL','UR','L','R','U','ALL'],
['UR','U','R','ALL'],
['UL','DR','L','U','D','ALL'],
['UR','DR','DL','UL','U','R','D','L','ALL'],
['UR','DR','R','D','ALL'],
['DL','L','D','ALL'],
['DL','DR','D','R','L','ALL'],
['DR','D','R','ALL'],
[],
[],
[],
[],
[]
]



pin_lists = []
state = Clock(np.array([]), np.array([1,1,1,1]))


state = np.zeros(14)
test_state = np.array([1,2,3,4,11,10,4,1,7,11,5, 0, 5, 10])
print(state)

