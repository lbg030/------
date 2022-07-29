from collections import deque

n, m = map(int, input().split())
limit = m//2
q = deque([(n,1)])
temp = []
minCnt = float("inf")
flag = 0
while q:
    values,cnt = q.popleft()
    
    if values == m:
        minCnt = min(minCnt, cnt)
        flag = 1
        continue
    
    double,plus= values * 2, int(str(values) + '1')
    
    if double <= m:
        q.append((double, cnt+1))
        
    if plus <= m:
        q.append((plus, cnt+1))
    
print(minCnt if flag else "-1")