from sys import stdin
from itertools import combinations

while True:
    n = list(map(int, stdin.readline().rstrip().split()))
    if (n[0] == 0):
        break
    # print(n)
    k, n = n[0], n[1:]

    li = list(combinations(n, 6))
    for x in li:
        print(*x)
    print()
