from collections import deque

n, l, r = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    result = []
    result.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and open[nx][ny] == 0:
                if l <= abs(lst[nx][ny] - lst[x][y]) <= r:
                    open[nx][ny] = 1    #open을 1로 지정함으로써 반복요소 제거
                    q.append([nx, ny])
                    result.append([nx, ny])
    return result


while True:
    open = [[0] * n for i in range(n)]
    flag = False
    
    for i in range(n):
        for j in range(n):
            if open[i][j] == 0:
                open[i][j] = 1
                result = bfs(i, j)
                
                if len(result) > 1:
                    flag = True
                    
                    num = sum([lst[x][y] for x, y in result]) // len(result)
                    for x, y in result:
                        lst[x][y] = num
    if not flag:
        break
    cnt += 1
    
print(cnt)