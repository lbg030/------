from collections import deque
import math

N, L = map(int, input().split())

cnt = 0 
lst= []


for _ in range(N):
    a,b = map(int, input().split())
    lst.append((a,b))
    
lst.sort()
location = lst[0][0]
lst= deque(lst)

while lst:
    a,b = lst.popleft()
    