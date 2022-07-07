from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False] * 100001
q = deque()
q.append([n, 0])

min_count = sys.maxsize

while q:
    cur, count = q.popleft()
    visited[cur] = True

    if cur == k:
        min_count = min(min_count, count)

    if 0 <= cur + 1 < 100001 and not visited[cur + 1]:
        q.append([cur + 1, count + 1])
    if 0 <= cur - 1 < 100001 and not visited[cur - 1]:
        q.append([cur - 1, count + 1])
    if 0 <= cur * 2 < 100001 and not visited[cur * 2]:
        q.append([cur * 2, count])

print(min_count)