# 2. 간선 정보가 없는 노드도 연결 요소로 포함
# 예시 테스트 케이스

# 6 2
# 3 4
# 4 2

# 2,3,4가 연결된 상태라서 정답이 1개가 아님
# 1,5,6도 단일 노드로 존재하여 답이 4가됨.
from sys import stdin
from collections import deque

def bfs(start):
    lst = deque()
    lst.append(start)
    
    while lst:
        a = lst.popleft()
        for i in range(1, N+1):
            if graph[a][i] == 1:
                lst.append(i)
                graph[a][i] = graph[i][a] = 0
                visited[a-1] = True
                visited[i-1] = True
N, M = map(int , input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
cnt = 0
for _ in range(M):
    x,y = map(int, stdin.readline().rstrip().split()) 
    graph[x][y]= graph[y][x] = 1
visited = [False] * (N)
for i in range(1,N+1):
    for j in range(1, N+1):
        if graph[i][j] == 1 :
            bfs(i)
            cnt += 1
# print(graph)
# print(visited)
# print(visited.count(False))
print(cnt + visited.count(False))

    