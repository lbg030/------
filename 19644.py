from sys import stdin
from collections import deque
roadLength = int(input())
rifleLength, damage = map(int, input().split())
mine = int(input())
zombie = deque([])
# 마인이 몇개 필요한지
cnt = 0
for i in range(roadLength):
    zombie.append([i+1, int(stdin.readline().rstrip())])

# print(f"원래 좀비 = {zombie}")
# 빡구현말고 논리적으로 풀어보기
for i, x in zombie:
    if i < rifleLength:
        if damage * (i - cnt) < x:
            cnt += 1
        # print(i, damage * (i - cnt))
    else:
        if (rifleLength - cnt) * damage < x:
            cnt += 1
        # print(i, (rifleLength - cnt) * damage)
    # print(i, (rifleLength - cnt) * damage)
    # print(i, x, cnt)
if cnt > mine:
    print('NO')
else:
    print('YES')
