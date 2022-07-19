n,m = map(int, input().split())
graph = [[0] * m for _ in range(n)]

#시계 방향
dx = [0,1,0,-1]
dy = [1,0,-1,0]
x,y = 0,0
d = 0
num = 1
graph[0][0] = 1
while True : 
    if num >= n*m:
        break
    
    nx = x + dx[d]
    ny = y + dy[d]
    
    # print(nx,ny)
    # print(graph)
    # print(graph[nx][ny]) # 2 1
    if 0<= nx < n and 0<= ny < m and not graph[nx][ny]:
        num += 1
        graph[nx][ny] = num
        x,y = nx, ny
    
    else :
        d += 1
        
    if d >= 4 :
        d = d % 4
        
    
    
for x in graph:
    print( *x)