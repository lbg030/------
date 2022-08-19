from sys import stdin
n, m = map(int, input().split())
graph = [list(map(str, stdin.readline().rstrip())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1,-1, 0, 0]

res = 0
dic = {}
dic[str(graph[0][0])] = True


def dfs(x,y,cnt):
    global res
    res = max(res, cnt)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0<= nx < n and 0 <= ny < m:
            if str(graph[nx][ny]) not in dic:
                dic[str(graph[nx][ny])] = True
                dfs(nx,ny,cnt + 1)
                # dfs 가 끝나면 visited에 있던 항목들을 dfs하기 전으로 되돌려야 하기 때문에 remove
                del(dic[str(graph[nx][ny])]) 

dfs(0,0,1)
print(res)