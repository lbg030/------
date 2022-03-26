from sys import stdin
from collections import deque

n = int(input())
li = sorted(deque(map(int, stdin.readline().split())))

m = int(input())
li2 = deque(map(int, stdin.readline().split()))
dic = {}

for x in li:
    if(x not in dic):
        dic[(x)] = 1
    else:
        dic[(x)] += 1

# print(dic)
for x in li2:
    if x in dic:
        # print(f"x={x}")
        print(dic[x], end=" ")
    else:
        # print(f"x={x}")
        print("0", end=" ")
