# 반드시 첫 번째 사람이 X를 놓고 두 번째 사람이 O를 놓는다. 
# 어느 때든지 한 사람의 말이 가로, 세로, 대각선 방향으로 3칸을 잇는 데 성공하면 게임은 즉시 끝난다. 게임판이 가득 차도 게임은 끝난다.


# 게임이 끝날 조건 = valid
# 1. X가 5개 O가 4개 였을 경우
# 2. X나 O가 한줄(가로, 세로, 대각선)을 차지했을경우


def Tic_Tac_Toe(x_cnt, o_cnt, lst):
    flag = 0
    for i in range(4):
        if lst[i] == 'X':
            if i == 0:
                if (lst[i] == lst[i+1] == lst[i+2]) or (lst[i] == lst[i+3] == lst[i+6]) or(lst[i] == lst[i+4] == lst[i+8]):
                    flag = 1
                    break
            
            elif i == 1:
                if (lst[i] == lst[i+3] == lst[i+6]) :
                    flag = 1
                    break
            
            elif i == 2:
                if (lst[i] == lst[i+2] == lst[i+4]) or (lst[i] == lst[i+3] == lst[i+6]):
                    flag = 1
                    break
            
            elif i == 3:
                if (lst[i] == lst[i+1] == lst[i+2]):
                    flag = 1
                    break
                
        elif lst[i] == 'O':
                if i == 0:
                    if (lst[i] == lst[i+1] == lst[i+2]) or (lst[i] == lst[i+3] == lst[i+6]) or(lst[i] == lst[i+4] == lst[i+8]):
                        flag = 2
                        break
                    
                elif i == 1:
                    if (lst[i] == lst[i+3] == lst[i+6]) :
                        flag = 2
                        break
                
                elif i == 2:
                    if (lst[i] == lst[i+2] == lst[i+4]) or (lst[i] == lst[i+3] == lst[i+6]):
                        flag = 2
                        break
                    
                elif i == 3:
                    if (lst[i] == lst[i+1] == lst[i+2]):
                        flag = 2
                        break
            
    if lst[6] == 'X':
        if lst[6] == lst[7] == lst[8] :
            flag = 1
            
    elif lst[6] == 'O':
        if x_cnt == o_cnt:
            if lst[6] == lst[7] == lst[8]:
                flag = 1
                
    if (flag == 2 and x_cnt == o_cnt) or (flag == 1 and x_cnt > o_cnt):
        # print(flag)
        return ('valid')
    
    else:
        return ('invalid')
    

while True:
    lst = list(input())
    
    #end 종료
    if len(lst) == 3:
        # print('invalid')
        break
    
    x_cnt = lst.count('X')
    o_cnt = lst.count('O')
    
    # case 1. x가 5개 O가 4개 있을 경우
    if x_cnt == 5 and o_cnt == 4:
        # print("1", lst)
        print("valid")
        continue
    
    elif x_cnt < o_cnt or x_cnt - o_cnt > 1:
        # print("2", lst)
        print("invalid")
        continue
    
    else:
        # print("3", lst)
        print(Tic_Tac_Toe(x_cnt, o_cnt,lst))
    