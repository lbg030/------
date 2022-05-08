# 이동을 먼저 하고 그 전에 것을 지운다.
# temp 사용 하면 될 꺼 같은데
from collections import deque
from sys import stdin

n = int(stdin.readline())
li = deque(enumerate(map(int, input().split())))
# print(li)
ans = []

while li:
    idx, value = li.popleft()
    ans.append(idx+1)
    if(value > 0):

        # 이미 popleft()를 했기 때문에 왼쪽으로 한칸 옮겨 진것.
        # 만약 value가 1이었으면 이미 popleft()됐기 때문에 옮겨진 상태이기 때문에 그대로 출력하면 됨.

        li.rotate(-(value-1))
    else:
        li.rotate(-value)

    print(li)
print(*ans)
