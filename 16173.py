import sys
input = sys.stdin.readline

N = int(input())  # 게임구역크기 N

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

# 방문체크
visit = [[0] * N for _ in range(N)]

queue = [[0, 0]]

#하, 우
dx = [1, 0]
dy = [0, 1]

# BFS
while queue:
    x, y = queue[0][0], queue[0][1]
    del queue[0]

    # 맨 오른쪽 아래 도달하면 HaruHaru 출력
    if board[x][y] == -1:
        print("HaruHaru")
        exit(0)

    # 점프값
    jump = board[x][y]

    # 아래, 오른쪽 탐색
    for i in range(2):
        nx = x + dx[i] * jump
        ny = y + dy[i] * jump

        # 범위 안에 있고, 방문하지 않았으면 방문 체크 후 queue에 넣기
        if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            queue.append([nx, ny])


print("Hing")
