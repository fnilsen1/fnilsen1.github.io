let algs = 
["R U' R' U2 R U' R'", "R U' R' U' R U2 R'", "F D F' U F D' F'", "F' U' F U2 F' U' F", "U2 F D F' U' F D' F'", "U2 F' U2 F U' F' U' F", "U' F D F' U2 F D' F'", "R U' R' U R' F R F'", "R U' R' U2 R U' R' U", "R U' R' U2 R U' R' U2", "R U' R' U2 R U' R' U'", "R U' R' U' R U2 R' U", "R U' R' U' R U2 R' U2", "R U' R' U' R U2 R' U'", "R' D' F' U' F U D R", "F D F' U F D' F' U", "F D F' U F D' F' U2", "F D F' U F D' F' U'", "F' U' F U2 F' U' F U", "F' U' F U2 F' U' F U2", "F' U' F U2 F' U' F U'", "D' F R U2 R' U2 F' D", "U2 F U D R U' R' D' F'", "U2 F D F' U' F D' F' U", "U2 F D F' U' F D' F' U2", "U2 F D F' U' F D' F' U'", "U2 F' U2 F U' F' U' F U", "U2 F' U2 F U' F' U' F U2", "U2 F' U2 F U' F' U' F U'", "U' F D F' U2 F D' F' U", "U' F D F' U2 F D' F' U2", "U' F D F' U2 F D' F' U'", "U' D R' U2 F' U2 F R D'", "R U' R' U R' F R F' U", "R U' R' U R' F R F' U2", "R U' R' U R' F R F' U'", "R U' R' F' U' F R U2 R'", "R F' R' F U F' R F R'", "R2 U2 R F' R' U2 R F R", "R2 U2 R' F R2 F' R' U2 R2", "R' D' F' U' F U D R U", "R' D' F' U' F U D R U2", "R' D' F' U' F U D R U'", "F U F' R F U' F' U R'", "F R' F' R2 U2 R2 F R F'", "F' U F R' F R F2 U' F", "F' R' F U' F' U R U' F", "F' R' F' U' F2 U F' R F", "D F' D2 F U2 F' D2 F D'", "D2 R' D2 R U R' D2 R D2", "D2 F' D F U2 F' D' F D2", "D' R' D R U R' D' R D", "D' F R U2 R' U2 F' U D", "D' F R U2 R' U2 F' U2 D", "D' F R U2 R' U2 F' U' D", "U R U' R U2 R' U' R U' R2", "U R' F R2 F' U' F' U F R'", "U F R' F' R2 U' R2 F R F'", "U F D' F U2 F' D F U2 F2", "U F D' F U' F' D F U F2", "U F2 D' F U F' D F U' F", "U D R D R' U' R D' R' D'", "U D R' U2 R U' R' U' R D'", "U D F' D2 F U F' D2 F D'", "U D2 F' D F U F' D' F D2", "U D' F U' R U' R' U F' D", "U D' F U' F' U2 F U' F' D", "U D' F U' F' U' F U2 F' D", "U2 R U' R2 F R F' R U R'", "U2 R U' F U R' U' R F' R'", "U2 R U' F U F' R' F U' F'", "U2 R F' R' F U' F' R F R'", "U2 R2 U R' U R U2 R' U R'", "U2 R2 U2 R F R2 F' R U2 R2", "U2 F U D R U' R' D' F' U", "U2 F U D R U' R' D' F' U2", "U2 F U D R U' R' D' F' U'", "U2 F' U F' D' F U' F' D F2", "U2 F' R U2 F U F' U R' F", "U2 D R D R' U2 R D' R' D'", "U2 D2 R' D2 R U' R' D2 R D2", "U2 D' R' D R U' R' D' R D", "U' R U R2 U2 R2 U R2 U R", "U' R U' F U R U' R' F' R'", "U' R F' R' F U2 F' R F R'", "U' F U D F' U F U2 D' F'", "U' F R' F R U2 R U2 R' F2", "U' F' U2 F R U' R' F' U' F", "U' F' R U2 R' U' R U' R' F", "U' D R D R' U R D' R' D'", "U' D R' U2 F' U F U R D'", "U' D R' U2 F' U2 F R U D'", "U' D R' U2 F' U2 F R U2 D'", "U' D R' U2 F' U2 F R U' D'", "U' D R' U' R U2 R' U' R D'", "U' D F' D2 F U' F' D2 F D'", "U' D2 R' D2 R U2 R' D2 R D2", "U' D2 F' D F U' F' D' F D2", "U' D' R' D R U2 R' D' R D", "U' D' F U R U R' U2 F' D", "R U2 F U R' U' R F' U2 R'", "R U' R2 F' U' F U R2 U R'", "R U' R' U2 R' F R F2 U F", "R U' R' U2 F' U F R U' R'", "R U' R' U2 F' U2 F R U' R'", "R U' R' U2 F' U' F R U' R'", "R U' R' U' F R' F' R2 U2 R'", "R U' R' F' U' F U' R U' R'", "R U' R' F' U' F R U2 R' U", "R U' R' F' U' F R U2 R' U2", "R U' R' F' U' F R U2 R' U'", "R F U' R' U2 R U F' U2 R'", "R F U' R' U' R U F' U R'", "R F D' F' U F D F' U' R'", "R F D' F' U2 F D F' U2 R'", "R F D' F' U' F D F' U R'", "R F' R' F U F' R F R' U", "R F' R' F U F' R F R' U2", "R F' R' F U F' R F R' U'", "R2 U2 R F' R' U2 R F R U", "R2 U2 R F' R' U2 R F R U2", "R2 U2 R F' R' U2 R F R U'", "R2 U2 R' F R2 F' R' U2 R2 U", "R2 U2 R' F R2 F' R' U2 R2 U2", "R2 U2 R' F R2 F' R' U2 R2 U'", "R2 D' F' U F D F' U' F R2", "R' F' D2 F U F' D2 F U' R", "R' D' F' U' F D F' U F R", "F U R D2 R' U' R D2 R' F'", "F U F' R F U' F' U R' U", "F U F' R F U' F' U R' U2", "F U F' R F U' F' U R' U'", "F U D F R' F' R U' D' F'", "F U' R D2 R' U R D2 R' F'", "F R' F' R2 U2 R2 F R F' U", "F R' F' R2 U2 R2 F R F' U2", "F R' F' R2 U2 R2 F R F' U'", "F R' F' R2 U2 R' U R U' R'", "F R' F' R2 U2 R' U2 R U2 R'", "F' U F U R U' R' F' U' F", "F' U F R' F R F2 U' F U", "F' U F R' F R F2 U' F U2", "F' U F R' F R F2 U' F U'", "F' U2 R' U' F' U F R U2 F", "F' U2 F U2 R U R' F' U' F", "F' U2 F U2 F' U' F2 R' F' R", "F' R' U R U' F U R' U' R", "F' R' U2 R U2 F U2 R' U2 R", "F' R' U2 R U2 F U' R' U R", "F' R' U' R U' R' U2 R U' F", "F' R' F U' F' U R U' F U", "F' R' F U' F' U R U' F U2", "F' R' F U' F' U R U' F U'", "F' R' F' U' F R F R' U R", "F' R' F' U' F2 U F' R F U", "F' R' F' U' F2 U F' R F U2", "F' R' F' U' F2 U F' R F U'", "F' R' D' F2 D R2 U' R' U2 F", "D F' D2 F U2 F' D2 F U D'", "D F' D2 F U2 F' D2 F U2 D'", "D F' D2 F U2 F' D2 F U' D'", "D2 R' U' D2 F' U F D2 R D2", "D2 R' D2 R U R' D2 R U D2", "D2 R' D2 R U R' D2 R U2 D2", "D2 R' D2 R U R' D2 R U' D2", "D2 F' D F U2 F' D' F U D2", "D2 F' D F U2 F' D' F U2 D2", "D2 F' D F U2 F' D' F U' D2", "D' R' U' D F' U F D' R D", "D' R' D R U R' D' R U D", "D' R' D R U R' D' R U2 D", "D' R' D R U R' D' R U' D", "D' R' D F D' R D R' F' R", "U R U R' U' R U' R2 F R F'", "U R U R' U' F' U2 F R U2 R'", "U R U2 F' U' F2 D R2 D' F' R'", "U R U' R U2 R' U' R U' R2 U", "U R U' R U2 R' U' R U' R2 U2", "U R U' R U2 R' U' R U' R2 U'", "U R U' F U2 F' U' F U' F' R'", "U R F U2 F' U' F U' F' U' R'", "U R2 F' U F D' F' U' F D R2", "U R' U' F2 D2 F U F' D2 F2 R", "U R' F R D' R' D F' D' R D", "U R' F R2 F' U' F' U F R' U", "U R' F R2 F' U' F' U F R' U2", "U R' F R2 F' U' F' U F R' U'", "U R' F2 U' R F2 R' U F' R F'", "U R' F2 R D' R' D F2 D' R D", "U F U2 F' U2 R U2 F U2 F' R'", "U F U' F' U R U' F U F' R'", "U F R U R' D R U' R' D' F'", "U F R U2 R' D R U2 R' D' F'", "U F R F' U' F R' F' R2 U' R2", "U F R' F' R F' U2 F R U2 R'", "U F R' F' R2 U' R2 F R F' U", "U F R' F' R2 U' R2 F R F' U2", "U F R' F' R2 U' R2 F R F' U'", "U F R' F' R2 U' R' U R U' R'", "U F R' F' R2 U' R' U2 R U2 R'", "U F R' D R' D' R2 F' R U' R'", "U F D' F U2 F' D F U2 F2 U", "U F D' F U2 F' D F U2 F2 U2", "U F D' F U2 F' D F U2 F2 U'", "U F D' F U' F' D F U F2 U", "U F D' F U' F' D F U F2 U2", "U F D' F U' F' D F U F2 U'", "U F2 U2 R D2 R' U2 R D2 R' F2", "U F2 D' F U F' D F U' F U", "U F2 D' F U F' D F U' F U2", "U F2 D' F U F' D F U' F U'", "U F' U2 R' F R F' U2 F' U2 F2", "U F' U2 F2 R' F' R U' F' U' F", "U F' U' R' D R U R' D' R F", "U F' U' F R U2 R' U2 F' U' F", "U D R D R' U' R D' R' U D'", "U D R D R' U' R D' R' U2 D'", "U D R D R' U' R D' R' U' D'", "U D R' U2 R U' R' U' R U D'", "U D R' U2 R U' R' U' R U2 D'", "U D R' U2 R U' R' U' R U' D'", "U D F' D2 F U F' D2 F U D'", "U D F' D2 F U F' D2 F U2 D'", "U D F' D2 F U F' D2 F U' D'", "U D2 F' D F U F' D' F U D2", "U D2 F' D F U F' D' F U2 D2", "U D2 F' D F U F' D' F U' D2", "U D' F U' R U' R' U F' U D", "U D' F U' R U' R' U F' U2 D", "U D' F U' R U' R' U F' U' D", "U D' F U' F' U2 F U' F' U D", "U D' F U' F' U2 F U' F' U2 D", "U D' F U' F' U2 F U' F' U' D", "U D' F U' F' U' F U2 F' U D", "U D' F U' F' U' F U2 F' U2 D", "U D' F U' F' U' F U2 F' U' D", "U2 R U R2 F R F' U2 F' U' F", "U2 R U F U F' U F U2 F' R'", "U2 R U2 F R U R' U' F' U2 R'", "U2 R U' R2 F R F' R U R' U", "U2 R U' R2 F R F' R U R' U2", "U2 R U' R2 F R F' R U R' U'", "U2 R U' R' F' U F U R U' R'", "U2 R U' R' F' U F U2 R U2 R'", "U2 R U' R' F' U F R' F R F'", "U2 R U' R' F' U' F U R U R'", "U2 R U' F U R' U' R F' R' U", "U2 R U' F U R' U' R F' R' U2", "U2 R U' F U R' U' R F' R' U'", "U2 R U' F U F' R' U F U2 F'", "U2 R U' F U F' R' F U' F' U", "U2 R U' F U F' R' F U' F' U2", "U2 R U' F U F' R' F U' F' U'", "U2 R U' F U' R' U R U F' R'", "U2 R U' F R' F' R U R U' R2", "U2 R U' F D' F' U F D F' R'", "U2 R F' R' F U' F' R F R' U", "U2 R F' R' F U' F' R F R' U2", "U2 R F' R' F U' F' R F R' U'", "U2 R F' D2 F U F' D2 F U' R'", "U2 R2 U R F' U' F U R' U2 R2", "U2 R2 U R' U R U2 R' U R' U", "U2 R2 U R' U R U2 R' U R' U2", "U2 R2 U R' U R U2 R' U R' U'", "U2 R2 U R' F' U' F U R U2 R2", "U2 R2 U2 R F R2 F' R U2 R2 U", "U2 R2 U2 R F R2 F' R U2 R2 U2", "U2 R2 U2 R F R2 F' R U2 R2 U'", "U2 R' U R U F' R' U2 R U2 F", "U2 R' U' R F' U' R' U2 R U F", "U2 R' F R F U2 R' F R U2 F2", "U2 F U R' D R U' R' D' R F'", "U2 F U F' R F R U' R' F' R'", "U2 F U2 R' D R U2 R' D' R F'", "U2 F R F2 U R' U' R F2 R' F'", "U2 F R2 F' U R2 U' F R F' R", "U2 F' U F2 U R U' R' F2 U' F", "U2 F' U F' D' F U' F' D F2 U", "U2 F' U F' D' F U' F' D F2 U2", "U2 F' U F' D' F U' F' D F2 U'", "U2 F' U2 R' F U' F' U R U2 F", "U2 F' U2 F R U2 R' U2 F' U2 F", "U2 F' U2 F R U2 R' U' F' U F", "U2 F' U2 F R U2 R' F R' F' R", "U2 F' U' R D2 R' U R D2 R' F", "U2 F' U' F R U R' U2 F' U' F", "U2 F' R U2 F U F' U R' F U", "U2 F' R U2 F U F' U R' F U2", "U2 F' R U2 F U F' U R' F U'", "U2 D R D R' U2 R D' R' U D'", "U2 D R D R' U2 R D' R' U2 D'", "U2 D R D R' U2 R D' R' U' D'", "U2 D R' U2 R' F R F' U2 R D'", "U2 D2 R' D2 R U' R' D2 R U D2", "U2 D2 R' D2 R U' R' D2 R U2 D2", "U2 D2 R' D2 R U' R' D2 R U' D2", "U2 D' R' D R U' R' D' R U D", "U2 D' R' D R U' R' D' R U2 D", "U2 D' R' D R U' R' D' R U' D", "U' R U R2 U2 R2 U R2 U R U", "U' R U R2 U2 R2 U R2 U R U2", "U' R U R2 U2 R2 U R2 U R U'", "U' R U R2 U' D' F2 U F2 D R", "U' R U2 F U2 F' R' U F U F'", "U' R U2 F U' R' U2 R U F' R'", "U' R U2 F D' F' U2 F D F' R'", "U' R U2 D' F2 U2 F2 D R2 U R", "U' R U' F U R U' R' F' R' U", "U' R U' F U R U' R' F' R' U2", "U' R U' F U R U' R' F' R' U'", "U' R F R2 U R2 U' R2 F' U R'", "U' R F' R' F U2 F' R F R' U", "U' R F' R' F U2 F' R F R' U2", "U' R F' R' F U2 F' R F R' U'", "U' R' F R F2 U F U F' U' F", "U' F U F' U' R U2 F U2 F' R'", "U' F U D F' U F U2 D' F' U", "U' F U D F' U F U2 D' F' U2", "U' F U D F' U F U2 D' F' U'", "U' F R D2 R' U R U' D2 R' F'", "U' F R D2 R' U R D2 R' U' F'", "U' F R2 D2 R' U R D2 R2 U' F'", "U' F R' F R U2 R U2 R' F2 U", "U' F R' F R U2 R U2 R' F2 U2", "U' F R' F R U2 R U2 R' F2 U'", "U' F2 U F' U R U' R' F U' F2", "U' F' U F R U' R' U F' U' F", "U' F' U2 F U' R' F R F2 U' F", "U' F' U2 F R U' R' F' U' F U", "U' F' U2 F R U' R' F' U' F U2", "U' F' U2 F R U' R' F' U' F U'", "U' F' U' R' F U' F' U R U F", "U' F' R U2 R' U' R U' R' F U", "U' F' R U2 R' U' R U' R' F U2", "U' F' R U2 R' U' R U' R' F U'", "U' D R D R' U R D' R' U D'", "U' D R D R' U R D' R' U2 D'", "U' D R D R' U R D' R' U' D'", "U' D R' U2 F' U F U R U D'", "U' D R' U2 F' U F U R U2 D'", "U' D R' U2 F' U F U R U' D'", "U' D R' U' R U2 R' U' R U D'", "U' D R' U' R U2 R' U' R U2 D'", "U' D R' U' R U2 R' U' R U' D'", "U' D F' D2 F U' F' D2 F U D'", "U' D F' D2 F U' F' D2 F U2 D'", "U' D F' D2 F U' F' D2 F U' D'", "U' D2 R' D2 R U2 R' D2 R U D2", "U' D2 R' D2 R U2 R' D2 R U2 D2", "U' D2 R' D2 R U2 R' D2 R U' D2", "U' D2 F' D F U' F' D' F U D2", "U' D2 F' D F U' F' D' F U2 D2", "U' D2 F' D F U' F' D' F U' D2", "U' D' R' D R U2 R' D' R U D", "U' D' R' D R U2 R' D' R U2 D", "U' D' R' D R U2 R' D' R U' D", "U' D' F U R U R' U2 F' U D", "U' D' F U R U R' U2 F' U2 D", "U' D' F U R U R' U2 F' U' D", "R U R U2 R2 U' R2 U' R' U' R'", "R U R' U F2 U2 R' F2 R U2 F2", "R U F U' R' U R U F' U' R'", "R U F R' F' U F R F' U' R'", "R U F R' F' R' F D R D' F'", "R U2 R' U2 R2 U2 F R' F' U2 R2", "R U2 F U R' U' R F' U2 R' U", "R U2 F U R' U' R F' U2 R' U2", "R U2 F U R' U' R F' U2 R' U'", "R U2 F R U R2 U' R F' U2 R'", "R U' R2 F D' F D F2 R2 U R'", "R U' R2 F' U' F U R2 U R' U", "R U' R2 F' U' F U R2 U R' U2", "R U' R2 F' U' F U R2 U R' U'", "R U' R2 D' R U2 R' D R2 U' R'", "R U' R2 D' R U' R' D R2 U2 R'", "R U' R' U R' U' F U R U' F'", "R U' R' U R' F R2 U R' U' F'", "R U' R' U F' U2 F U R U R'", "R U' R' U2 R U R' U' R U' R'", "R U' R' U2 R2 D R' U' R D' R2", "R U' R' U2 R' F R F2 U F U", "R U' R' U2 R' F R F2 U F U2", "R U' R' U2 R' F R F2 U F U'", "R U' R' U2 R' F D R' D' R2 F'", "R U' R' U2 R' F D' F D F2 R", "R U' R' U2 F' U F U R U2 R'", "R U' R' U2 F' U F R U' R' U", "R U' R' U2 F' U F R U' R' U2", "R U' R' U2 F' U F R U' R' U'", "R U' R' U2 F' U2 F U R U2 R'", "R U' R' U2 F' U2 F R U' R' U", "R U' R' U2 F' U2 F R U' R' U2", "R U' R' U2 F' U2 F R U' R' U'", "R U' R' U2 F' U' F U R U2 R'", "R U' R' U2 F' U' F R U' R' U", "R U' R' U2 F' U' F R U' R' U2", "R U' R' U2 F' U' F R U' R' U'", "R U' R' U' R U' R' U R U2 R'", "R U' R' U' R2 D R' U2 R D' R2", "R U' R' U' R' U' R2 U' R2 U2 R", "R U' R' U' R' F R F' R U2 R'", "R U' R' U' F R' F' R2 U2 R' U", "R U' R' U' F R' F' R2 U2 R' U2", "R U' R' U' F R' F' R2 U2 R' U'", "R U' R' U' F' U F U2 R U' R'", "R U' R' U' F' U F U' R U2 R'", "R U' R' F' U' F U2 R' F R F'", "R U' R' F' U' F U' R U' R' U", "R U' R' F' U' F U' R U' R' U2", "R U' R' F' U' F U' R U' R' U'", "R U' R' F' U' F2 R' F' R2 U2 R'", "R U' F R' F' U' F R F' U2 R'", "R U' F' R' F U2 F' R F U' R'", "R U' F' R' F U' F' R F U2 R'", "R F U F R2 F' R2 U' F' U' R'", "R F U' R' U2 R U F' U2 R' U", "R F U' R' U2 R U F' U2 R' U2", "R F U' R' U2 R U F' U2 R' U'", "R F U' R' U' R U F' U R' U", "R F U' R' U' R U F' U R' U2", "R F U' R' U' R U F' U R' U'", "R F R F2 U' F2 R' F' R U' R2", "R F R2 F' R' U' R F R2 F' R'", "R F R2 F' R' U' R2 U R2 U' R2", "R F R' D R2 D' R' F' R U' R2", "R F D' F' U F D F' U' R' U", "R F D' F' U F D F' U' R' U2", "R F D' F' U F D F' U' R' U'", "R F D' F' U2 F D F' U2 R' U", "R F D' F' U2 F D F' U2 R' U2", "R F D' F' U2 F D F' U2 R' U'", "R F D' F' U' F D F' U R' U", "R F D' F' U' F D F' U R' U2", "R F D' F' U' F D F' U R' U'", "R F2 U R2 D R' D' R' U' F2 R'", "R F2 R2 F' R U' R' F R2 F2 R'", "R F' U2 R2 D' F2 D R2 U2 F R'", "R D2 F U' F' U' F U2 F' D2 R'", "R D2 F R U2 R' U2 F' U2 D2 R'", "R2 U R F' R' U' R F R' U' R2", "R2 U R' U R U2 R2 U2 R U' R'", "R2 U R' U R U2 R2 U' R U2 R'", "R2 U R' U' R' U' F R F' U2 R'", "R2 U R' D' R U R' D R U2 R2", "R2 U R' D' R U2 R' D R U R2", "R2 U F' U' F U2 F' U' F U2 R2", "R2 U2 R F' R' U R F R' U R2", "R2 U2 R F' R' U2 R U' F U R", "R2 U2 R2 U' R U R U2 R' U R'", "R2 U' R2 F' R' U R U' F2 R F'", "R2 F2 U R' U R U2 F2 R' U R'", "R2 F2 U2 R F R2 F' R U2 F2 R2", "R2 D' R2 U R U' R2 D R2 U R'", "R2 D' R2 U R D' F2 D F2 D R'", "R2 D' F' U F D F' U' F R2 U", "R2 D' F' U F D F' U' F R2 U2", "R2 D' F' U F D F' U' F R2 U'", "R' U R D R' U2 R D' R' U R", "R' U2 R D R' U R D' R' U R", "R' U2 R2 F U R2 U' F' R2 U2 R", "R' U' R' U' R U R U F R F'", "R' U' R' U' R2 U R U R2 U' R'", "R' U' R' U' R' U R U R2 U2 R'", "R' U' R' U' R' U R' U' R2 U2 R", "R' U' F' D2 F U2 F' D2 F U' R", "R' F R U R U' R' F' R U R'", "R' F R U2 F U' F U F' U2 F'", "R' F R F D' F' D F' R2 U' R2", "R' F R2 U R' U' F' U R U' R'", "R' F R2 U R' U' F' U2 R U2 R'", "R' F R2 U R' U' F' R' F R F'", "R' F D R' D' R2 F' U R U' R'", "R' F D R' D' R2 F' U2 R U2 R'", "R' F D R' D' R2 F' R' F R F'", "R' F2 R2 F U' F' R2 F2 R2 U R'", "R' F2 R' U2 R' F R U2 R F2 R", "R' F2 R' U2 F U F' U R F2 R", "R' F' U2 F D' F' U F U D R", "R' F' R U R U' R' F R U R'", "R' F' R2 U F U2 F' U' R2 F R", "R' F' D2 F U F' D2 F U' R U", "R' F' D2 F U F' D2 F U' R U2", "R' F' D2 F U F' D2 F U' R U'", "R' D' R' F R F' D F R' F' R2", "R' D' F' U' F D R U' R' U2 R", "R' D' F' U' F D F' U F R U", "R' D' F' U' F D F' U F R U2", "R' D' F' U' F D F' U F R U'", "R' D' F' U' F' U F2 D R2 U2 R'", "F U R D2 R' U' R D2 R' F' U", "F U R D2 R' U' R D2 R' F' U2", "F U R D2 R' U' R D2 R' F' U'", "F U R' U' F' U R U' R U R'", "F U F2 U F U' F U' R' F' R", "F U F2 U F2 U2 F' U2 F' U' F", "F U F' D' F U F' D F U2 F'", "F U D R U R' D' R U2 R' F'", "F U D F R' F' R U' D' F' U", "F U D F R' F' R U' D' F' U2", "F U D F R' F' R U' D' F' U'", "F U2 F U F U' F U F2 U F'", "F U' R D2 R' U R D2 R' F' U", "F U' R D2 R' U R D2 R' F' U2", "F U' R D2 R' U R D2 R' F' U'", "F U' R2 D2 R' U R D2 R2 U F'", "F U' R' D' F U' D F U R F2", "F U' F' D' F U' F' D F U2 F'", "F R U R' U' D F' U2 F D' F'", "F R U R' D F' U F U2 D' F'", "F R F U R' U R U2 F' R' F'", "F R F U' F' U2 R' U2 F U F2", "F R' F' R2 U2 R' U R U' R' U", "F R' F' R2 U2 R' U R U' R' U2", "F R' F' R2 U2 R' U R U' R' U'", "F R' F' R2 U2 R' U2 R U2 R' U", "F R' F' R2 U2 R' U2 R U2 R' U2", "F R' F' R2 U2 R' U2 R U2 R' U'", "F D R U R' U' F' U2 F D' F'", "F D R U R' F' U F U2 D' F'", "F D R U' R' U R U R' D' F'", "F D F2 D2 F U F' D2 F2 D' F'", "F D F' U F U D' R U' R' F'", "F D F' U F D' R U R' U' F'", "F D F' U2 F U R U' R' D' F'", "F2 U F U F2 U2 F U F2 U F'", "F2 R U2 R' F' R' F R2 U2 R' F2", "F2 D' F U' F' D F2 U2 F' U' F", "F' U R U2 R' U' R U' R' U2 F", "F' U F U R U' R' F' U' F U", "F' U F U R U' R' F' U' F U2", "F' U F U R U' R' F' U' F U'", "F' U F U' F' U' F U F' U' F", "F' U F' U' F U' F' U2 F U2 F", "F' U F' U' F2 U' F2 U2 F U2 F", "F' U2 R U2 R' U' R U' R' U F", "F' U2 R' U' F' U F R U2 F U", "F' U2 R' U' F' U F R U2 F U2", "F' U2 R' U' F' U F R U2 F U'", "F' U2 F U R' F2 D' F' D F' R", "F' U2 F U2 R U R' F' U' F U", "F' U2 F U2 R U R' F' U' F U2", "F' U2 F U2 R U R' F' U' F U'", "F' U2 F U2 F' U' F U2 F' U2 F", "F' U2 F U2 F' U' F U' F' U F", "F' U2 F U2 F' U' F2 R' F' R U", "F' U2 F U2 F' U' F2 R' F' R U2", "F' U2 F U2 F' U' F2 R' F' R U'", "F' U2 F2 U2 F U' F2 U F' U2 F'", "F' U2 F' U2 F' U F' U' F U2 F2", "F' U' R' U' F2 R' F2 R U R F", "F' U' F U R' U' F' U F2 R F'", "F' U' F U R' F2 D' F' D R F'", "F' U' F U2 F' U F U F' U F", "F' U' F U2 F' U2 F U' F' U2 F", "F' U' F U' R U2 R' U2 F' U2 F", "F' U' F U' R U2 R' U' F' U F", "F' U' F U' R U2 R' F R' F' R", "F' U' F2 U R' U' F2 U F2 R F'", "F' U' F2 U2 F' U' F U' R' F' R", "F' R U' D2 F U' F' U2 D2 R' F", "F' R2 U2 R2 U2 R' F2 R2 F2 R' F", "F' R2 F2 R F2 R F U2 R' U2 R", "F' R2 F2 R F2 R F U' R' U R", "F' R' U R U' F U R' U' R U", "F' R' U R U' F U R' U' R U2", "F' R' U R U' F U R' U' R U'", "F' R' U R U' F2 U R' U' R F'", "F' R' U2 R U2 F U2 R' U2 R U", "F' R' U2 R U2 F U2 R' U2 R U2", "F' R' U2 R U2 F U2 R' U2 R U'", "F' R' U2 R U2 F U' R' U R U", "F' R' U2 R U2 F U' R' U R U2", "F' R' U2 R U2 F U' R' U R U'", "F' R' U2 R F' R' F U2 F' R F2", "F' R' U' R U' R' U2 R U' F U", "F' R' U' R U' R' U2 R U' F U2", "F' R' U' R U' R' U2 R U' F U'", "F' R' U' R F R' F' U F2 R F'", "F' R' U' R F2 R' F2 U F2 R F'", "F' R' U' R F' R' F U F' R F2", "F' R' U' F U F' R F2 R' F' R", "F' R' F U F2 U' F2 U' F' R F", "F' R' F D R2 U' R2 D' F' R F", "F' R' F2 U F2 U' F2 U' R U2 F", "F' R' F2 U' R F' R' F' U F' R", "F' R' F2 R F U' F2 U' F2 U F2", "F' R' F2 R F U' F' R' F2 R F", "F' R' F2 R F D' F2 D R2 U' R2", "F' R' F2 D R2 U' R2 D' R U2 F", "F' R' F' U' F R F U' R' U2 R", "F' R' F' U' F R F R' U R U", "F' R' F' U' F R F R' U R U2", "F' R' F' U' F R F R' U R U'", "F' R' D' F U' F' U D R U' F", "F' R' D' F2 D R2 U' R' U2 F U", "F' R' D' F2 D R2 U' R' U2 F U2", "F' R' D' F2 D R2 U' R' U2 F U'", "D R D' R U2 R' D R U2 R2 D'", "D R D' R U' R' D R U R2 D'", "D R2 D' R U R' D R U' R D'", "D R' F' U2 F2 R' F' R U2 R D'", "D F2 R2 F' R' F R' F' R' F' D'", "D F2 D2 F U2 F' D2 F U2 F D'", "D F' U' D2 F U' F' U2 D2 F D'", "D2 R' U' D2 F' U F D2 R U D2", "D2 R' U' D2 F' U F D2 R U2 D2", "D2 R' U' D2 F' U F D2 R U' D2", "D2 F2 D F U2 F' D' F U2 F D2", "D2 F' U' D F U' F' U2 D' F D2", "D' R F U2 R' U' R U' F' R' D", "D' R' U' D F' U F D' R U D", "D' R' U' D F' U F D' R U2 D", "D' R' U' D F' U F D' R U' D", "D' R' D F D' R D R' F' R U", "D' R' D F D' R D R' F' R U2", "D' R' D F D' R D R' F' R U'", "D' F U F2 U2 F2 U F2 U F D", "D' F U2 F2 U2 R' F2 R U2 F D", "D' F R U2 R' U' R U' R' F' D", "D' F R U2 R' F' U' F U' F' D", "D' F R2 U2 R2 U' R2 U' R2 F' D", "D' F2 R' F' R U2 R' F R F2 D"]

function rateAlgs(algs) {
    console.log(algs.sort((a, b) => {return rateAlg(b) - rateAlg(a);}));
}

function rateAlg(moves) {
    let allMoves = [["U", "D", "E", "y"], ["R", "L", "M", "x"], ["F", "B", "S", "z"]];

    let moveArr = moves.trim().split(" ");
    let len = moveArr.length;
    let result = len;
    let regripState = {
        "U": 0,
        "D": 0,
        "R": 0,
        "L": 0,
        "F": 0,
        "B": 0,
    };

    function axis(m) {
        if (m === "U" || m === "D" || m === "E" || m === "Y") {
            return 0;
        }
        else if (m === "R" || m === "L" || m === "M" || m === "X") {
            return 1;
        }
        else if (m === "F" || m === "B" || m === "S" || m === "Z") {
            return 2;
        }
    }

    function isRotation(m) {
        return (m === "X" || m === "Y" || m === "Z");
    }

    function isSlice(m) {
        return (m === "M" || m === "E" || m === "S");
    }

    function isBadMove(m) {
        return (m === "D" || m === "B" || m === "L");
    }

    function checkRegrip(m) {
        if (m === "F") {
            if (regripState["R"] % 4 === 0 || regripState["R"] % 4 === 2) {
                result -= 5*len/100;
            }
            else if (regripState["R"] % 4 === 1) {
                result -= 2*len/100;
            }
        }
        else if (m === "B") {
            if (regripState["R"] % 4 === 0 || regripState["R"] % 4 === 2) {
                result -= 5*len/100;
            }
            else if (regripState["R"] % 4 === 3) {
                result -= 2*len/100;
            }
        }
        else if (m === "R" && regripState["R"] % 4 === 2) {
            result -= 5*len/100;
        }
        else if (m === "L" && regripState["L"] % 4 === 2) {
            result -= 5*len/100;
        }
    }

    for (let i = 0; i < len; i++) {
        let mv = moveArr[i].toUpperCase();
        let m = mv[0];
        let me = mv.length === 1 || mv.includes("w") ? "*" : mv[mv.length - 1];

        if (isRotation(m)) {
            result -= (me === "2" ? 2 : 1) * len / 100;

            regripState = {
                "U": 0,
                "D": 0,
                "R": 0,
                "L": 0,
                "F": 0,
                "B": 0,
            };
        }
        else if (isBadMove(m)) {
            regripState[m] += me === "*" ? 3 : me === "2" ? 2 : 1;
        }
        else {
            regripState[m] += me === "*" ? 1 : me === "2" ? 2 : 3;
        }
        
        checkRegrip(m);

        if (i >= 1) {
            let pmv = moveArr[i - 1];
            let pm = pmv[0];
            let pme = pmv.length === 1 || pmv.includes("W") ? "*" : pmv[pmv.length - 1];

            if (axis(m) === axis(pm)) {
                if (me === pme) {
                    result -= 10*axis(m)*len/100;
                }
                else {
                    result -= 5*axis(m)*len/100;
                }
            }
            
            if (i >= 2) {
                let ppmv = moveArr[i - 2];
                let ppm = ppmv[0];
                let ppme = ppmv.length === 1 || ppmv.includes("W") ? "*" : ppmv[ppmv.length - 1];
            
                if (axis(m) === axis(ppm) && axis(m) !== 0 && m !== ppm) {
                    result -= 10*len/100;
                }
            }
        }
    }
    return (result*100/len).toFixed(2)
    // $("#result").text("Score: " + (result*100/len).toFixed(2));
}
