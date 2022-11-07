n = int(input())
m = int(input())

graph = [[False] * (n+1) for _ in range(n+1)]
visited= [[False] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    
    graph[a][b] = graph[b][a] = True
    
    
    
def bfs(n):
    q = [n]
    # res = []
    cnt = 0
    
    while q:
        for _ in range(1,n+1):
            pass
        
# print(graph)