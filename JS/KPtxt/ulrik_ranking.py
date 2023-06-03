file_name = r'JS\KPtxt\sledge.txt'
# move_scores = {
#     "R": 1,
#     "R'": 1,
#     "R2": 2,
#     "L": 3,
#     "L'": 3,
#     "L2": 4,
#     "U": 1,
#     "U'": 1,
#     "U2": 2,
#     "D": 2,
#     "D'": 2,
#     "D2": 4,
#     "F": 2,
#     "F'": 2,
#     "F2": 4,
#     "B": 4,
#     "B'": 4,
#     "B2": 5
# }

move_scores = {
    "R": 1,
    "R'": 1,
    "R2": 2,
    "L": 2,
    "L'": 2,
    "L2": 3,
    "U": 1,
    "U'": 1,
    "U2": 2,
    "D": 2,
    "D'": 2,
    "D2": 4,
    "F": 2,
    "F'": 2,
    "F2": 4,
    "B": 4,
    "B'": 4,
    "B2": 5
}

# alg scorer
def score_alg(alg,move_scores):
    score = 0
    list_moves = alg.split(" ")
    for move in list_moves:
        score += move_scores[move]
    return score

# alg ranker
def alg_ranker(algs,move_scores,N,prnt=True):
    '''
    algs: list of algs
    N: number of algs we will display
    '''
    N = min(len(algs),N)
    scores = {}
    for alg in algs:
        scores[alg] = score_alg(alg,move_scores)
    
    best_N = sorted(scores.items(), key=lambda x:x[1])[:N]
    
    if prnt:
        for i,alg in enumerate(best_N):
            print(f"{i+1}. {alg[0]}")
    
    return best_N
def rank_algs_from_file(file_name,exclude_U_before):
    with open(file_name) as my_file:
        read_algs = my_file.read().split('\n')
        algs = []
        for alg in read_algs:
            if exclude_U_before:
                if "'" in alg and alg[0] != "U": 
                    algs += [alg]
            else:
                if "'" in alg and (alg[-1] != "U" or alg[-2] != "U"): 
                    algs += [alg]
    alg_ranker(algs,move_scores,50)
    
rank_algs_from_file(file_name,True)