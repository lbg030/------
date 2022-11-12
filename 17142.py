from itertools import combinations
from collections import deque

def bfs(q):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] != 1:
                q.append((nx,ny))
                visited[nx][ny] = 1
                mini_graph[nx][ny] = mini_graph[x][y] + 1
            
n , m =map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [1, -1, 0, 0] 
dy = [0, 0, -1, 1]

two_position_list = []

# 예제 7번 대비
zero_count = 0
virus_movable = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            two_position_list.append((i,j)) # 2의 index 저장

        if graph[i][j] != 1:
            virus_movable += 1

# 활성화 시킬 바이러스 위치 경우의 수
two_combination_list = list(combinations(two_position_list, m))
# print(two_position_list)
res = float('inf')

# 활성화 시킬 바이러스 위치 ( m 개씩 )
for position in two_combination_list:
    visited = [[0] * n for _ in range(n)]
    mini_graph = [[-1] * n for _ in range(n)]
    q = deque()
    cnt = 0
    for i,j in position:
        mini_graph[i][j] = 0
        visited[i][j] = 1
        q.append([i,j])

    bfs(q)
    
    for flag in visited: 
        cnt += flag.count(1)
        
    if virus_movable == cnt:
        
        max_position_value = 0
        for row in range(n):
            for column in range(n):
                if graph[row][column] != 1 and (row, column) not in two_position_list:
                    max_position_value = max(max_position_value, mini_graph[row][column])

        res = min(max_position_value, res)
print(res if res != float('inf') else -1)