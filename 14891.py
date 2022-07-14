# N극은 0, S극은 1로 나타나있다.
# 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
# 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
# 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
# 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
# 12시방향부터 시계방향 순서대로 주어진다. 
# 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향이다. 
# 방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.

# deque로 rotate(1) 혹은 rotate(-1) 사용
# k <= 100이기 때문에 readline 필요없음
from collections import deque

gear = [deque(list(map(int, input()))) for _ in range(4)] # 톱니바퀴

t = int(input()) # 몇 번 회전시킬건지

case = [list(map(int, input().split())) for _ in range(t)]

# print(Gear, case)

for lst in case:
    gearNumber, rotation = lst[0], lst[1]
    