# 이동을 먼저 하고 그 전에 것을 지운다.
# temp 사용 하면 될 꺼 같은데
from collections import deque

n = int(input())
li = deque(enumerate(map(int, input().split())))
# print(li)
ans = []

while li:
    idx, value = li.popleft()
    ans.append(idx+1)
    if(value > 0):
        li.rotate(-(value-1))
    else:
        li.rotate(-value)

print(*ans)
