from sys import stdin
from collections import deque

n, l = map(int, input().split())
q = list(map(int, stdin.readline().rstrip().split()))
q = deque(sorted(q))
cnt = 0 
while q :
    k = q.popleft()
    maximum = k + l
    while True and q:
        if q[0] < maximum :
            q.popleft()
        else :
            break
        
    cnt += 1
    
print(cnt)
## 양옆에 0.5씩 거리를 둔다는게 무슨 의미 인지 모르겠음 