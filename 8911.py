# (x축 max - min) * y축(max - min) 하면 됨
import turtle


n = int(input())

for _ in range(n):
    lst = input()
    x, y = [], []
    turtleFaced = ['front', 'left', 'right ', 'behind']
    direction = turtleFaced[0]
    for x in lst:
        if x == 'F':
