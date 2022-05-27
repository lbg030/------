from sys import stdin
from collections import deque

N, M = map(int , input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
cnt = 0
for _ in range(M):
    x,y = map(int, stdin.readline().rstrip().split()) 
    graph[x][y]= graph[y][x] = 1

for i in range(1,N+1):
    for j in range(1, N+1):
        if graph[i][j] == 1 :
            bfs(i)
            cnt += 1
print(graph)

def bfs(start):
    lst = deque()
    lst.append(start)
    
    while lst:
        a = lst.popleft()
        for i in range(N+1):
            if graph[a][i] == 1:
                lst.append(i)
                graph[a][i] = graph[i][a] = 0
    