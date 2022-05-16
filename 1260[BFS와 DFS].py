# DFS BFS

n, m, start = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    n1,n2 = map(int, input().split())
    graph[n1][n2] = graph[n2][n1] = 1

print(graph)

#좀 더 쉬움
def dfs(start):
    pass


def bfs(start):
    pass