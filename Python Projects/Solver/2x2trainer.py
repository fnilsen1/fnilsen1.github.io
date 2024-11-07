from twobytwo_solver import solve, inverse
import random

auf = [" ", " U", " U'", " U2"]
with open("learn_algs.txt") as file:
    algs = file.readlines()

while True:
    # print((algs[random.randint(0,len(algs)-1)].strip()+auf[random.randint(0, 3)]).strip())
    solution = (algs[random.randint(0,len(algs)-1)].strip()+auf[random.randint(0, 3)]).strip()
    print(solution)
    scramble = solve(solution)
    pause = input()