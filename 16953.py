from collections import deque

n, m = map(int, input().split())
limit = m//2
q = deque([[n]])
cnt = 0
temp = []
flag = 0 
while q:
    values = q.popleft()
    for value in values:
        if value == m:
            flag = 1
            break
        
        elif value <= limit+1:
            temp.append(value * 2)
            temp.append(int(str(value) + '1'))
            
    if temp :
        cnt += 1
        q.append(temp)
        temp = []

    if flag:
        break

print(cnt if flag else "-1")