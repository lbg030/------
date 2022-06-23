from sys import stdin
from collections import deque
n,m = map(int, input().split())

lst = [list(map(int, stdin.readline().rstrip().split())) for i in range(m)]

#안되는 경우 cnt로 판별
cnt = 0
templist = deque()

dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(m):
    for j in range(n):
        if lst[i][j] == 1 :
            templist.append((i,j))
            
while cnt <= n:
    while templist:
        y, x = templist.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > n or ny > m:
                

# print(templist)