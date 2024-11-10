def func(computer):
    x,y = [], []
    flag_D = False
    for i in range(len(computer)):
        for j in range(len(computer[0])):
            if computer[i][j] == 'D':
                flag_D = True
                x.append(i)
                y.append(j)
    if flag_D == False:
        return 0 # D가 하나도 없는 경우
    
    board =  [min(x), min(y), max(x)+1, max(y)+1]
    return ' '.join(map(str, board))