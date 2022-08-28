import sys
from collections import deque
import math
from itertools import combinations

n = int(sys.stdin.readline())
populations = list(map(int, sys.stdin.readline().split()))
populations.insert(0, 0)

maps = [[0 for _ in range(n+1)] for _ in range(n+1)]

# 주어진 그룹의 모든 원소가 서로 연결되어 있는지 확인하는 함수
# start: 그룹의 시작점, candidate : 그룹의 모든 구성원
def is_group(start, maps, candidates):
    queue = deque()
    queue.append(start)
    count = 1
    visited = set()
    while queue:
        y = queue.popleft()
        visited.add(y)
        for x in range(len(maps[y])):
            if maps[y][x] == 1 and x in candidates and x not in visited:
                queue.append(x)
                visited.add(x)
                count += 1            
    if count == len(candidates):
        return True
    return False

for y in range(1, n+1):
    adj_list = list(map(int, sys.stdin.readline().split()))
    for x in adj_list[1:]:
        maps[y][x] = 1

max_value = math.inf


for i in range(1, (n // 2 + 1)):
    candidates = combinations(range(1, n+1), i)
    # 1. 그룹 그분
    for one in candidates:
        one = list(one)
        other = list(set(range(1,n+1)) - set(one))
        # 2. 각 그룹별로 bfs를 시행하며 연결여부를 확인한다.
        if is_group(one[0], maps, set(one)) is True and is_group(other[0], maps, set(other)) is True:
            # 3. 두 개의 그룹 모두 연결되어 있을 경우, 인구차를 구한다.
            one_value = [populations[i] for i in one]
            other_value = [populations[i] for i in other]
            max_value = min(max_value, abs(sum(one_value) - sum(other_value)))

if max_value == math.inf:
    print(-1)
else:
    print(max_value)