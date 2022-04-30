# 보드 크기와 테스트 케이스 개수
size, case = map(int, input().split())

# 보드판
board = [[0] + list(map(int, input().split())) for _ in range(size)]

for i in range(size):
    for j in range(size+1):
        if i == 0 and j == 0:
            continue
        elif i != 0 and j == 0:
            board[i][j] = board[i-1][-1]

        else:
            board[i][j] = board[i][j-1] + board[i][j]

for _ in range(case):
    x1, y1, x2, y2 = map(int, input().split())
    second = board[x2-1][y2]
    first = board[x1-1][y1-1]
    # print(second, first)
    if x1 == 1 and y1 == 1:
        result = second
    elif x1 == x2 and y1 == y2:
        result = second - board[x1-1][y1-2]
    else:
        result = second - first
    print(result)
print(board)
