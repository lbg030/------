import heapq
from sys import stdin
n = int(input())

lst = []

for _ in range(n):
    n = int(stdin.readline())
    if(n == 0):
        if(len(lst) == 0):
            print("0")
        else:
            print(heapq.heappop(lst))

    else:
        heapq.heappush(lst, n)
