from collections import deque

n, m = map(int, input().split())
graph = []

# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    queue = deque()
    queue.append((0,0,0))

    while queue:
        x,y,cnt = queue.popleft()
        
        # 끝 점에 도달하면 이동 횟수를 출력
        if x == n - 1 and y == m - 1:
            return visited[x][y][cnt]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
            if graph[nx][ny] == 1 and cnt == 0 :
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
            elif graph[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                queue.append((nx, ny, cnt))
    return -1

print(bfs())
# print(visited)
