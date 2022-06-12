from sys import stdin
from itertools import combinations_with_replacement

n, m = map(int, input().split())
lst = sorted(list(map(int, stdin.readline().rstrip().split())))

li = combinations_with_replacement(lst,m)

for x in li:
    print(*x)