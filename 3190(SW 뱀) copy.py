# 뱀의 머리는 처음에 오른쪽
# 자기 자신한테 닿거나 벽에 닿으면 사망

from ast import Pass
from collections import deque

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 시간
count = 0

size = int(input())
# 보드 판 [ 모두 0으로 초기화 ]
board = [[0] * size for _ in range(size)]

# 초기 뱀 머리 방향
snakeHead = deque(['R', 'S', 'L', 'N'])


apple = int(input())
# 사과 위치
for _ in range(apple):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1
sec = deque()
way = deque()
# 뱀이 방향 전환 할 위치
moving = int(input())
for _ in range(moving):
    second, direction = input().split()
    sec.append(int(second))
    way.append(direction)

# print(board, sec, way)

# 뱀 이동 코드

snakeLocation = deque([[0, 0]])
while True:
    x, y = snakeLocation[-1][0], snakeLocation[-1][1]
    snakeHeading = snakeHead[0]
    if snakeHeading == 'R':  # 동
        move = [x, y+1]

    elif snakeHeading == 'S':  # 남
        move = [x+1, y]

    elif snakeHeading == 'L':  # 서
        move = [x, y-1]

    elif snakeHeading == 'N':  # 북
        move = [x-1, y]

    # 사과 먹은거
    # if board[x][y] != 1:
    #     snakeLocation.popleft()

    # 벽에 닿거나 뱀끼리 닿았을 때
    if(x >= size or y >= size or x < 0 or y < 0):
        print(count)
        break

    # 움직인거 카운트 and 뱀 위치 삽입
    else:
        if(move not in snakeLocation):
            count += 1  # 뱀 이동
            # print(f" x = {x} y = {y}")
            snakeLocation.append(move)
            if board[x][y] != 1:
                snakeLocation.popleft()

            # 사과를 먹었을 때 0으로 초기화
            else:
                board[x][y] = 0

        else:
            count += 1
            print(count)
            break

    # 정해진 시간에 방향 전환
    if sec:
        if sec[0] == count:
            if way[0] == 'D':
                snakeHead.rotate(-1)
            elif way[0] == 'L':
                snakeHead.rotate(1)

            sec.popleft()
            way.popleft()

    # print(f"snakeLocation = {snakeLocation} and count = {count}")
