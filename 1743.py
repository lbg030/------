from collections import deque

length,width,trash = map(int, input().split())

graph = [[0] * (width+1) for _ in range(length+1)]
check = [[False] * (width+1) for _ in range(length+1)]

for _ in range(trash):
    x, y = map(int, input().split())
    graph[x][y] = 1

#쓰래기 개수
result = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    cnt = 0
    queue = deque([(x,y)])
    while queue:
        
        x, y = queue.popleft()
        check[x][y] = True
        cnt += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < length+1 and 0<= ny < width +1 :
                if graph[nx][ny] == 1 and check[nx][ny] == False:
                    queue.append((nx,ny))
    
    return cnt  

for i in range(1, length+1):
    for j in range(1, width+1):
        if graph[i][j] == 1 and check[i][j] == False:
            result = max(result, bfs(i,j))
            
print(result)