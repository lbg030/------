from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
queue = deque()
#시작값
queue.append((0,0))
#이미 갔다는 표시로 1로 변경
graph[0][0] = 1
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

#그래프 시작
while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        #처음 받아올 때 값은 str값인 "1"
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == "1":
            queue.append((nx,ny))
            graph[nx][ny] = graph[x][y] + 1
    # print(x,y, queue)
print(graph[n-1][m-1])