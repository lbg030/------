# 반드시 첫 번째 사람이 X를 놓고 두 번째 사람이 O를 놓는다. 
# 어느 때든지 한 사람의 말이 가로, 세로, 대각선 방향으로 3칸을 잇는 데 성공하면 게임은 즉시 끝난다. 게임판이 가득 차도 게임은 끝난다.


# 게임이 끝날 조건 = valid
# 1. X가 5개 O가 4개 였을 경우
# 2. X나 O가 한줄(가로, 세로, 대각선)을 차지했을경우

while True:
    lst = list(input())
    
    #end 종료
    if len(lst) == 3:
        print('invalid')
        break
    
    x_cnt = lst.count('X')
    o_cnt = lst.count('O')
    
    # case 1. x가 5개 O가 4개 있을 경우
    if x_cnt == 5 and o_cnt == 4:
        print("valid")
        continue