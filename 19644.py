from sys import stdin
from collections import deque
roadLength = int(input())
rifleLength, damage = map(int, input().split())
mine = int(input())
zombie = deque([])
# 마인이 몇개 필요한지
cnt = 0
check = 0
for i in range(roadLength):
    zombie.append([i+1, int(stdin.readline().rstrip())])

# print(f"원래 좀비 = {zombie}")
# 빡구현말고 논리적으로 풀어보기
for i, x in zombie:
    if i < rifleLength:
        if damage * (i - check) < x:
            cnt += 1
            check += 1
        # print(i, damage * (i - check))
    else:
        if (rifleLength - check) * damage < x:
            cnt += 1
            check += 1
        # print(i, (rifleLength - check) * damage)
    # print(i, (rifleLength - check) * damage)
    # print(i, x, cnt)

    # 만약에 0인 좀비가 나왔을 때에는 거리를 한칸 버는 셈이므로 빼준다
    if check > 0:
        if x == 0:
            check -= 1

if cnt > mine:
    print('NO')
else:
    print('YES')
