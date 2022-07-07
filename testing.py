from collections import deque

n, m = map(int ,input().split())
maximum = 100001
visited = [0] * maximum 

def bfs(n):
    q = deque()
    q.append(n)
    
    while q : 
        x = q.popleft()
        if x == m :
            print(visited[x])
            break
        if 0 <= x-1 < 100001 and visited[x-1] == 0:
            q.append(x-1)
            visited[x-1] = visited[x] + 1
        if 0 <= x*2 < 100001 and visited[x*2] == 0:
            q.append(x*2)
            visited[x*2] = visited[x]
        if 0 <= x+1 < 100001 and visited[x+1] == 0:
            q.append(x+1)
            visited[x+1] = visited[x] + 1

bfs(n)