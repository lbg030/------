# deque나 두개 리스트 써도 시간초과 발생
from sys import stdin

# 사람수
number = int(input())

# 현재 사람들의 키
people = []

# 스택에는 사용자의 키와, 몇명을 볼 수 있는지 넣음.
stack = []

# 몇명인지 세기
cnt = 0

# 사람 append
for _ in range(number):
    people.append(int(stdin.readline().rstrip()))

for x in people:
    # 스택이 존재하고 x가 마지막 사람보다 크다면 여기서 종료.
    while stack and stack[-1][0] < x:
        cnt += stack.pop()[1]  # 카운트 더해주기.

    # 만약 스택이 존재하지 않는다면 넣어주기
    if not stack:
        stack.append([x, 1])
        continue

    if stack[-1][0] == x:
        count = stack.pop()[1]
        cnt += count
        if stack:
            cnt += 1
        stack.append([x, count + 1])

    # 들어온 값이 전에 값 보다 작을 때 .
    else:
        stack.append([x, 1])
        cnt += 1
print(cnt)
