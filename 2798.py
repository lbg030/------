from sys import stdin
from itertools import combinations
n, m = map(int, input().split())

li = sorted(list(map(int, stdin.readline().split())), reverse=True)
# print(li)
total = 0

li2 = list(combinations(li, 3))
for x in li2:
    if(sum(x) <= m):
        total = max(sum(x), total)

print(total)
