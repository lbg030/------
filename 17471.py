N = int(input())

population = list(map(int, input().split()))
graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(1,N+1):
    tmp = list(map(int, input().split()))
    for x in tmp[1:]:
        graph[i][x] = graph[x][i] = 1

print(graph)