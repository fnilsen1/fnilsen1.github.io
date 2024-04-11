
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if digits == "":
        return[]

    dict ={
    2:["a","b","c"],
    3:["d","e","f"],
    4:["g","h","i"],
    5:["j","k","l"],
    6:["m","n","o"],
    7:["p","q","r","s"],
    8:["t","u","v"],
    9:["w","x","y","z"]
    }
    index_list = [0]*len(digits)
    start_list = index_list[:]
    index_list[0]=1
    combo_list = []
    combo_list.append(index_list[:])
    
    while index_list!=start_list:
        for i in range(len(digits)):
            index_list[i]+=1
            index_list[i]%=len(dict[int(digits[i])])
            if(index_list[i]):
                break
        combo_list.append(index_list[:])

    for i in range(len(combo_list)):
        for j in range(len(combo_list[i])):
            combo_list[i][j]=dict[int(digits[j])][combo_list[i][j]]
        combo_list[i]="".join(combo_list[i])
    print(combo_list)

letterCombinations("23")
