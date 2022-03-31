from sys import stdin
from itertools import combinations

n, s = map(int, input().split())
li = list(map(int, stdin.readline().rstrip().split()))

cnt = 1
res = 0
while cnt <= n:
    lst = list(combinations(li, cnt))
    for x in lst:
        if(sum(x) == s):
            res += 1
    cnt += 1

print(res)
