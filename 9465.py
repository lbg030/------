from sys import stdin
input = stdin.readline

n = int(input())

for _ in range(n):
    score = 0
    x = int(input())
    lst = [list(map(int, input().split())) for _ in range(2)]
    
    if x == 1:
        print(max(lst[0][0], lst[1][0]))
    
    else :
        lst[1][1] = lst[0][0] + lst[1][1]
        lst[0][1] = lst[1][0] + lst[0][1]
        for i in range(2, x):
            lst[0][i] += max(lst[1][i-1], lst[1][i-2])
            lst[1][i] += max(lst[0][i-1], lst[0][i-2])
            
        print(max(lst[0][-1], lst[1][-1]))
    
    # print(lst)
