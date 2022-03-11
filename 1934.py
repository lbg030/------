from math import lcm

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    print(lcm(x, y))
