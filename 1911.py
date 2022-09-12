from collections import deque
import math

N, L = map(int, input().split())
cnt = 0 
lst= []

for _ in range(N):
    a,b = map(int, input().split())
    lst.append((a,b))
    
lst.sort()
loc = lst[0][0]
lst= deque(lst)

while lst:
    a,b = lst.popleft()
    
    if b < loc :
        continue
    
    elif loc < a:
        loc = a
    # continue에 걸리지 않았으므로 무조건 한개 이상 깔아야함
    if (b - loc) % L == 0 :
        cnt += (b-loc) // L
        loc += L * ((b-loc)//L)
    else :
        cnt += math.ceil((b-loc)/L)
        loc += L * math.ceil((b-loc)/L)
        
print(cnt)