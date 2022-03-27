from sys import stdin

n = list(stdin.readline().rstrip())

n = sorted(n, reverse=True)

n = list(map(int, n))
# print(n)

if(0 not in n or sum(n) % 3 != 0):
    print("-1")
else:
    print(*n, sep='')
