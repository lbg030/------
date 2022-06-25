#white 는 내편 blue 는 상대편
#n**2
from sys import stdin
from collections import deque
n,m = map(int, input().split())

lst = [list(map(str, stdin.readline().rstrip())) for _ in range(m)]
graph = [[True] * n for _ in range(m)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

white = []
blue = []

def dfs(x,y, color):
    cnt = 1
    queue = deque()
    queue.append((x,y))
    graph[x][y] = False
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= m or ny >= n or nx < 0 or ny < 0 :
                continue
            else :
                if graph[nx][ny] == True and lst[nx][ny] == color:
                    graph[nx][ny] = False
                    queue.append((nx,ny))
                    cnt += 1
    if color == 'W':
        white.append(cnt)
    else :
        blue.append(cnt)
        

for i in range(m):
    for j in range(n):
        if graph[i][j] == True:
            dfs(i,j,lst[i][j])
wResult = 0
bResult = 0
for x in white:
    wResult += x**2

for x in blue:
    bResult += x**2
    
print(wResult,bResult)