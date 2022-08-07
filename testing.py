from collections import deque

field = [list(input()) for _ in range(12)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
res = 0 # 결과

flag = 1 # while 문을 돌리기 위한 초기값

def bfs(i,j):
    color = field[i][j]
    q = deque()
    q.append((i,j))
    removed = [(i,j)] #만약 길이가 4 이상이면 revmoed에 있는 좌표값으로 field에서 제거
    visited[i][j] = True
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0<= ny < 6: # 인덱스
                if field[nx][ny] == color and visited[nx][ny] == False: #색깔이 같고 방문하지 않은 곳이라면
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    removed.append((nx,ny))
    
    if len(removed) >= 4:
        for x,y in removed:
            field[x][y] = '.'
        return True
    
    # 길이가 4 미만
    else :
        return False


while flag > 0:
    flag = 0 # 변하지 않았다란 의미로 0으로 설정
    visited = [[False] * 6 for _ in range(12)] #visit은 while한번 할때마다 초기화 시켜줘야하기 때문에 여기에 위치
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.':
                flag += bfs(i,j) # True면 +1 False면 0 
                
    # 중력에 따라 내려가게 하기
    # 처음에는 위에서 아래로 하였으나 이렇게 하면 오류가 발생하게 되어 거꾸로 하는 것으로 변경
    for i in range(10,-1,-1):
        for j in range(5,-1,-1):
            if field[i][j] != '.' and field[i+1][j] == '.':  #특정 좌표가 . 이 아닌데 그 아래는 .인 경우 ( 중력을 받아야 하는 경우)
                for k in range(1,11-i+1): # 해당 점부터 맨 끝까지 탐색 
                    if field[i + k][j] != '.':
                        field[i+k-1][j] = field[i][j]
                        field[i][j] = '.'
                        break
                    
                    elif i+k == 11: # 예외처리 ( 마지막 까지 . 인 경우 )
                        field[i+k][j] = field[i][j]
                        field[i][j] = '.'
                            
    if flag > 0 :
        res += 1
    
print(res)