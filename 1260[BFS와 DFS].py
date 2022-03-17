from collections import deque

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    m1, m2 = map(int, input().split())

    graph[m1][m2] = graph[m2][m1] = 1


def bfs(start_v):
    discovered = [start_v]

    queue = deque()
    queue.append(start_v)

    while queue:

        v = queue.popleft()
        print(v, end=' ')

        for w in range(len(graph[start_v])):
            if graph[v][w] == 1 and (w not in discovered):
                discovered.append(w)
                queue.append(w)


def dfs(start_v, discovered=[]):

    discovered.append(start_v)
    print(start_v, end=' ')

    for w in range(len(graph[start_v])):
        if graph[start_v][w] == 1 and (w not in discovered):
            dfs(w, discovered)


dfs(V)
print()
bfs(V)
