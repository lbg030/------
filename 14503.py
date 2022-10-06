#둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.

N, M = map(int, input().split())
robot = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

clean = 0
x ,y, direction = robot[0],robot[1],robot[2]

# 왼쪽으로 회전
def left_move(x,y,direction):
    if direction == 0:
        return x,y-1,3
    
    elif direction == 1:
        return x-1,y,0
    
    elif direction == 2:
        return x, y+1,1
    
    else :
        return x+1,y,2
    
while True:
        # 청소할 상황이 있는 경우 
    if graph[x][y] == 0 and visited[x][y] == False:
        clean += 1
        visited[x][y] = True
        x,y,direction = left_move(x,y,direction)

        if 0 <= x < N and 0 <= y < M: # 범위 내에 속할 때 ( 즉 끝 벽이 아닐 때)
            if graph[x][y] == 1 or visited[x][y] == True: # 가고자 하는 방향이 벽이거나 이미 청소한 구역일 경우
                x,y,direction = left_move(x,y,direction)
    break

# 1번 상황 체크
