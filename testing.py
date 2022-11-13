from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    while a:
        x, y = a.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and s[nx][ny] != 1:
                visit[nx][ny] = 1
                a.append([nx, ny])
                cs[nx][ny] = cs[x][y] + 1
dx = [1, -1, 0, 0] 
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
s = []
q = []
b = 0
inf = 100000000
result = inf
for i in range(n):
    a = list(map(int, input().split()))
    s.append(a)
    for j in range(n):
        if a[j] == 2: q.append([i, j])
        if a[j] != 1: b += 1
cq = list(combinations(q, m))
for i in cq:
    cs = [[-1] * n for i in range(n)]
    visit = [[0] * n for i in range(n)]
    a = deque()
    for x, y in i:
        visit[x][y] = 1
        cs[x][y] = 0
        a.append([x, y])
    bfs()
    cnt = 0
    for j in visit: cnt += j.count(1)
    if b == cnt:
        print(cs)
        max_n = 0
        for j in range(n):
            for k in range(n):
                if s[j][k] != 1 and [j, k] not in q:
                    max_n = max(max_n, cs[j][k])
        result = min(result, max_n)
print(result if result != inf else -1)