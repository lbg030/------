from collections import deque

n,l,r = map(int, input().split())

#그래프
lst = [list(map(int, input().split())) for _ in range(n)]

#회수
cnt = 0 

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 방문했는지 체크용


def bfs(x,y):
    q = deque()
    result = []    #return할 result값
    q.append((x,y))
    result.append((x,y))
    visited[x][y] = True
    
    while q:
        a, b = q.popleft()
        for i in range(4):
            
            da = a + dx[i]
            db = b + dy[i]
            
            if 0 <= da < n and 0 <= db < n and visited[da][db] == False:
                if l <= abs(lst[da][db] - lst[a][b]) <= r :
                    q.append((da,db))
                    result.append((da,db))
                    visited[da][db] = True
    
    return result

while True :
    visited = [[False] * n for _ in range(n)]
    check = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
    
                result = bfs(i, j)
                
                #1개 이상이 존재한다는 뜻
                if len(result) > 1 :
                    check = 1
                    adding = 0
                    for x,y in result :
                        adding += lst[x][y]
                    adding = adding // len(result)
                    
                    for x,y in result:
                        lst[x][y] = adding
                        
    if check == 0:
        print(cnt)
        break
    cnt += 1