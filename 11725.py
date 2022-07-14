from sys import stdin
from collections import deque

## 트리는 2차원 배열로 설정해야함
n = int(input())

graph = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)
# print(parent)

def bfs(start):
    q = deque()
    q.append(start)
    
    while q :
        v = q.popleft()
        for i in graph[v]:
            if parent[i] == 0:
                parent[i] = v
                q.append(i)
bfs(1)
for x in parent[2:]:
    print(x)