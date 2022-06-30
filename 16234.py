n,l,r = map(int, input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

#옮겨야됨
open = [[False] * n for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1,-1, 0, 0]

while True :
    for i in range(n):
        for j in range(n):
            for k in range(4):
                
                x = i + dx[i]
                y = j + dy[i]
                
                if 0 <= x < n and 0 <= y < n:
                    if l < abs(graph[x][y] - graph[i][j]) < r :
                        
                        open[x][y] = open[y][x] = True #서로 연결되어있다는 의미
                        