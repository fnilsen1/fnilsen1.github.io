def størst_minst(liste):
    minst = liste[0]
    storst = liste[0]
    for i in liste:
        if i < minst:
            minst = i
        if i > storst:
            storst = i
    # print((storst, minst))
    return((storst, minst))


størst_minst([3, 5, 1, 8, 2]) 