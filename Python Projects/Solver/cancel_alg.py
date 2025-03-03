def cancel_alg(alg):
    ''' 
    cancels algs where each move has 1 character + ' or 2 
    '''
    moves = alg.split(" ")
    original_alg = alg
    alg = ""
    for i in range(len(moves)-1):
        if moves[i] and moves[i][0]==moves[i+1][0]:
            rot = 2
            if moves[i][-1]=="'": rot+=2
            if moves[i][-1]=="2": rot+=1
            if moves[i+1][-1]=="'": rot+=2
            if moves[i+1][-1]=="2": rot+=1
            rot %= 4
            extra = ""

            if rot:

                if rot==2:
                    extra = "2"
                if rot==3:
                    extra = "'"
                    
                moves[i+1] = moves[i][0]+extra

            else: # if cancels fully
                moves[i+1] = ""
        elif moves[i]:
            alg += moves[i] + " "
    
    if moves[-1]:
        alg += moves[-1]
    alg = alg.strip()

    if alg == original_alg:
        return alg 
    # if we cancelled moves, we might be able to cancel more if we run again
    return cancel_alg(alg)
