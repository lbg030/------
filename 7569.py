from sys import stdin
from collections import deque
n, m, h = map(int, input().split())

lst = [list(map(int, stdin.readline().rstrip().split())) for _ in range(m*h)]

cnt = 0
templist = deque()
temp = []


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(m*h):
    for j in range(n):
        if lst[i][j] == 1:
            temp.append((i, j))
    
templist.append(temp)


while templist :
    temp = []
    cnt += 1
    k = templist.popleft()
    for i in k:
        x,y = i
        
        #px mx는 상 하를 계산함.
        px = x + m
        mx = x - m
        
        if 0 <= px < m*h:
            if lst[px][y] == 0:
                lst[px][y] = 1
                temp.append((px,y))
                
        if 0 <= mx < m*h:
            if lst[mx][y] == 0:
                lst[mx][y] = 1
                temp.append((mx,y))
                
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m*h and 0 <= ny < n:
                if lst[nx][ny] == 0:
                    lst[nx][ny] = 1
                    temp.append((nx, ny))
                else :
                    continue
                
    if temp:
        templist.append(temp)
        
    # print(cnt)
    # print(lst)

flag = 1

for x in lst:
    if x.count(0) > 0 :
        flag = 0

print("-1" if flag == 0 else cnt-1)