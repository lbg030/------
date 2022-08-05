from collections import deque

field = [list(input()) for _ in range(12)]
# print(field)
flag = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

res = 0

def bfs(i,j):
    color = field[i][j]
    q = deque()
    q.append((i,j))
    removed = [(i,j)]
    cnt = 1
    visited[i][j] = True
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0<= ny < 6:
                if field[nx][ny] == color and visited[nx][ny] == False:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    removed.append((nx,ny))
                    cnt += 1
        # print(removed, color)
        # print(field)
    if cnt >= 4:
        for x,y in removed:
            field[x][y] = '.'
        return True
    
    else :
        return False


while flag > 0:
    flag = 0
    visited = [[False] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.':
                flag += bfs(i,j)
                
                    
    # print(field,res)
    # 중력에 따라 내려가게 하기
    for i in range(10,-1,-1):
        for j in range(5,-1,-1):
            if field[i][j] != '.' and field[i+1][j] == '.': 
                for k in range(1,11-i+1):
                    if field[i + k][j] != '.':
                        field[i+k-1][j] = field[i][j]
                        field[i][j] = '.'
                        break
                    
                    elif i+k == 11:
                        field[i+k][j] = field[i][j]
                        field[i][j] = '.'
                            
                # field[i+1][j] = field[i][j]
                # field[i][j] = '.'
    # print(field)
    res += 1
print(res-1)