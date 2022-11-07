def bfs(k):
    q = [k]
    res = []
    cnt = 0
    
    while q:
        number = q.pop()
        for i in range(1,n+1):
            if graph[number][i] == True and visited[number][i] == False:
                q.append(i)
                visited[number][i] = visited[i][number] = True
        res.append(number)
    
    res = len(set(res)) - 1
    return res


n = int(input())
m = int(input())

graph = [[False] * (n+1) for _ in range(n+1)]
visited= [[False] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    
    graph[a][b] = graph[b][a] = True
    
print(bfs(1))
    

    