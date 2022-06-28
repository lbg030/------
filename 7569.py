from sys import stdin
from collections import deque
n, m, l = map(int, input().split())

lst = [list(map(int, stdin.readline().rstrip().split())) for i in range(m*l)]


cnt = 0
templist = deque()
temp = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(m):
    for j in range(n):
        if lst[i][j] == 1:
            temp.append((i, j))
    
templist.append(temp)


while templist:
    temp = []
    cnt += 1
    # 3 과 5 가 들어감
    k = templist.popleft()
    for i in k:
        x,y = i
        # print(f"x = {x}, y = {y}")
        # print(f"templist {templist}")
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # print(x, y)
            if nx >= m or ny >= n or nx < 0 or ny < 0:
                continue
            else:
                if lst[nx][ny] == 0:
                    lst[nx][ny] = 1
                    temp.append((nx, ny))
                else : # 여기도 생각 다시 해봐야됨
                    continue
                
    #여기서 templist 요소 한번 사이클 끝
    # print(x,y, cnt)
    if temp:
        templist.append(temp)
        
    # print(templist)
    
flag = 1

for x in lst:
    if x.count(0) > 0 :
        flag = 0

if flag == 0 :
    print('-1')
else :
    print(cnt - 1)
