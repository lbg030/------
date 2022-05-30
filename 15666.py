from sys import stdin
from itertools import combinations_with_replacement
n, m = map(int, input().split())

lst = sorted(set(map(int ,stdin.readline().rstrip().split())))

li = combinations_with_replacement(lst, m)
# print(sorted(list(li)))
# print(lst)
for x in sorted(li):
    print(*x)