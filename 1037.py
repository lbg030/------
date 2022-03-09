from sys import stdin
from math import lcm

n = int(stdin.readline())

li = list(map(int, input().split()))
ans = 1
for x in li:
    ans = lcm(x, ans)
if(ans in li):
    ans = ans * min(li)
print(ans)
