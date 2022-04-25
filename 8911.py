# (x축 max - min) * y축(max - min) 하면 됨
from collections import deque


n = int(input())

for _ in range(n):
    lst = input()
    x, y = [0], [0]
    # front 북, right 동 left 서 behind 남
    turtleFaced = deque(['front', 'left', 'behind', 'right'])

    for e in lst:
        direction = turtleFaced[0]

        if e == 'F':
            if direction == "front":
                y.append(y[-1] + 1)
            elif direction == "left":
                x.append(x[-1] - 1)

            elif direction == "behind":
                y.append(y[-1] - 1)

            else:
                # print('여기')
                x.append(x[-1] + 1)

        elif e == 'B':
            if direction == "front":
                y.append(y[-1] - 1)
            elif direction == "left":
                x.append(x[-1] + 1)

            elif direction == "behind":
                y.append(y[-1] + 1)

            else:
                x.append(x[-1] - 1)

        elif e == 'R':
            turtleFaced.rotate(1)

        elif e == 'L':
            turtleFaced.rotate(-1)
        # print(f" e = {e}, direction = {direction}, x = {x}, y = {y}")
    print((max(x) - min(x)) * (max(y) - min(y)))
