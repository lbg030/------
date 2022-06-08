n = int(input())

graph = [ [0] * (n+1) for _ in range(n+1)]

lst = [list(map(str, input())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if lst[i][j] == '1':
            graph[i][j] = 1
# 총 몇단지 인지
cnt = 0



print(graph)