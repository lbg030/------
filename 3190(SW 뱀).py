# 해결 안됨.
# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 11, 0, 0]

size = int(input())
board = [[0] * size for _ in range(size)]
apple = int(input())
for _ in range(apple):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

moving = int(input())
for _ in range(moving):
    None
