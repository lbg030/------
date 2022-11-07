n = int(input())
m = int(input())

graph = [[False] * (n+1) for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    
    graph[a][b] = graph[b][a] = True
    
    
    
def bfs(n):
    