#둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.

N, M = map(int, input().split())
robot = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

x, y, direction = robot[0],robot[1],robot[2]

# 왼쪽으로 회전
dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited[x][y] = True
cnt = 1

while True:
    flag = False
    
    for _ in range(4):
        nx = x + dx[(direction + 3) % 4]
        ny = y + dy[(direction + 3) % 4]
        
        direction = (direction + 3) % 4
        
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and visited[nx][ny] == False:
            visited[nx][ny] = True
            cnt += 1
            x = nx
            y = ny
            
            flag = True
            break
    
    if not flag :
        if graph[x - dx[direction]][y -dy[direction]]:
            print(cnt)
            break
        else:
            x = x - dx[direction]
            y = y - dy[direction]