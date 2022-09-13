INF = float("inf") 

V, E = map(int, input().split())
start = int(input())


graph = [[INF] * (V+1) for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u][v] = w
    
print(graph)