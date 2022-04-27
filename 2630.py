# 정사각형으로 4분할 한다고 해서 쿼드트리라고 불린다고 한다 ..

size = int(input())

# board
board = [list(map(int, input().split())) for _ in range(size)]

# white = 0 , blue = 1
result = []


def solve(x, y, size):
    color = board[x][y]

    # X와 Y축 조사
    for i in range(x, x+size):
        for j in range(y, y+size):
            if color != board[i][j]:
                solve(x, y, size//2)
                print(
                    f"x ={x} y = {y}, i = {i}, j = {j}, size = {size}, color = {color}, result = {result}")
                solve(x, y + size//2, size//2)
                print(
                    f"x ={x} y = {y}, i = {i}, j = {j}, size = {size}, color = {color}, result = {result}")
                solve(x + size//2, y, size//2)
                print(
                    f"x ={x} y = {y}, i = {i}, j = {j}, size = {size}, color = {color}, result = {result}")
                solve(x + size//2, y+size//2, size//2)
                print(
                    f"x ={x} y = {y}, i = {i}, j = {j}, size = {size}, color = {color}, result = {result}")
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)


solve(0, 0, size)
print(result.count(0))
print(result.count(1))
# print(result)
