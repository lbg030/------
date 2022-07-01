from collections import deque
import sys

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < k and 0 <= ny < n and 0 <= nz < m:
                if a[nx][ny][nz] == 0 and c[nx][ny][nz] == 0:
                    q.append([nx, ny, nz])
                    a[nx][ny][nz] = 1
                    c[nx][ny][nz] = c[x][y][z] + 1

m, n, k = map(int, input().split())
a = [[list(map(int, input().split())) for _ in range(n)] for _ in range(k)]
c = [[[0]*m for _ in range(n)] for _ in range(k)]
q = deque()

for i in range(k):
    for j in range(n):
        for l in range(m):
            if a[i][j][l] == 1 and c[i][j][l] == 0:
                q.append([i, j, l])
                c[i][j][l] = 1

bfs()
for i in a:
    for j in i:
        if 0 in j:
            print(-1)
            sys.exit()
ans = 0
for i in c:
    for j in i:
        list_max = max(j)
        ans = max(ans, list_max)
print(ans-1)