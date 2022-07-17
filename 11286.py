import heapq
from sys import stdin
n = int(input())

H = []
for _ in range(n):
    value = int(stdin.readline())
    
    if value != 0 :
        heapq.heappush(H, (abs(value), value))
    else:
        if len(H) == 0 :
            print("0")
        else :
            print(heapq.heappop(H)[1])