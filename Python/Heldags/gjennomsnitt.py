def gjennomsnitt(liste):
    sum = 0
    for i in liste:
        sum+=i
    # print(round(sum/len(liste),2))
    return round(sum/len(liste),2)


gjennomsnitt([2, 5, 8, 10]) 