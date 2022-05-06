from sys import stdin
from collections import deque
roadLength = int(input())
rifleLength, damage = map(int, input().split())
mine = int(input())
zombie = deque([])

for i in range(roadLength):
    zombie.append([i+1, int(stdin.readline().rstrip())])

while True:
    print(zombie)
    if not zombie:
        print('Yes')
        break
    # 마인이 존재 할때에는 무조건 Yes임
    if mine:
        # 첫번째 좀비를 라이플로 못잡을 때는 mine 사용
        if zombie[0][1] > damage:
            mine -= 1
            zombie.popleft()
            continue

        # 마인을 쓸 필요가 없을 때는 데미지 감소 시키기 [ 첫번째는 무조건 죽기 때문에  ]
        else:
            for i in range(rifleLength):
                # 만약 리스트 길이 초과 시 멈춤
                if i > len(zombie):
                    break
                else:
                    zombie[i][1] -= damage
                    zombie.popleft()

            continue

    # 마인이 존재 x
    else:
        # 만약 첫번째 좀비를 라이플로 못죽이면 끝
        if zombie[0][1] > damage:

            print('No')
            break
        else:
            for i in range(rifleLength):
                # 만약 리스트 길이 초과 시 멈춤
                if i > len(zombie):
                    break
                else:
                    zombie[i][1] -= damage
                    zombie.popleft()
