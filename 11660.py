size, case = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(size)]
for i in range(size):

for i in range(size):
    for j in range(size):
        if(i == 0):
            board[i][j] = sum(board[i][:j+1])
        else:
            if j == 0:
                board[i][j] = board[i-1][size-1] + board[i][j]

for _ in range(case):
    x1, y1, x2, y2 = map(int, input().split())
