from collections import deque
n, m =map(int,input().split())

lst  = deque([n])
cnt = 0

if n == m :
    print(cnt)
else :
    while True :
        temp = []
        for x in lst:
            add = x + 1
            minus = x - 1
            teleport = x * 2
            temp.append(add)
            temp.append(minus)
            temp.append(teleport)
        cnt += 1
        
        if m in temp:
            print(cnt)
            break
        else :
            lst.extend(temp)
            lst.popleft()