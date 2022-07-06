n = input()
m = input()

# print(n,m)
graph = [[0] * (len(m) + 1) for _ in range(len(n) + 1)]

for i in range(1, (len(n) + 1)):
    for j in range(1, (len(m)+1)):
        if n[i-1] == m[j-1]:
            graph[i][j] = graph[i-1][j-1] + 1
        else :
            graph[i][j] = max(graph[i-1][j], graph[i][j-1])
            

print(graph[-1][-1])