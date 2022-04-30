# 보드 크기와 테스트 케이스 개수
size, case = map(int, input().split())

# 보드판
board = [list(map(int, input().split())) for _ in range(size)]

for i in range(size):
    for j in range(size):

        # 첫번째
        if(i == 0 and j == 0):
            continue

        else:
            if j == 0:
                board[i][j] = board[i-1][size-1] + board[i][j]
            else:
                board[i][j] = board[i][j-1] + board[i][j]

# 테스트 케이스 입력받고 출력
for _ in range(case):
    x1, y1, x2, y2 = map(int, input().split())
    result = 0
    if(x1 == 0 and y1 == 0):
        print(board[x2-1][y2-1])
    else:
        print(board[x2-1][y2] - board[x1-1][y1-1])

# print(board)
