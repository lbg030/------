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

# print(board)
for j in range(case):
    ans = 0
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2 :
        ans = board[x2-1][y2] - board[x2-1][y2-1]
    elif x1 == 1 and y1 == 1:
        ans = board[x2-1][y2]
    else :
        ans = board[x2-1][y2] - board[x1-1][y1]
        
    print(ans)
    # print(board)