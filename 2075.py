n = int(input())

lst = [list(map(int ,input().split())) for _ in range(n)]
cnt = 0
while  cnt < n :
    deleted = 0
     
    for i in range(n):
        if i == 0:
            deletedValue = lst[i][-1]
        else :
            if lst[i][-1] > deletedValue:
                deletedValue = lst[i][-1]
                deleted = i
    cnt += 1
    
    if cnt == n:
        print(lst[deleted].pop())
    else :
        lst[deleted].pop()