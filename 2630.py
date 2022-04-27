size = int(input())

# board
board = [list(map(int, input().split())) for _ in range(size)]


#white, blue
white, blue = 0, 0
check = []
# print(board)
for i in range(size):
    check.extend(set(board[i]))

if (len(set(check)) > 1):
    pass
else:
    if check[0] == 0:
        white += 1
    else:
        blue += 1

# print(white)
# print(blue)
