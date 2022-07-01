from collections import deque
n, m , h = map(int, input().split())

tomato = [[list(map(int, input().split())) for _ in range(m)] for _ in range(h)]
visited = [[[False] * n for _ in range(m)] for _ in range(h)]
dx = [1, -1, 0, 0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

cnt = 0

templist = deque()
temp = []

for i in range(h):
    for j in range(m):
        for k in range(n):
            if tomato[i][j][k] == 1 and visited[i][j][k] == False:
                temp.append((i,j,k))
                visited[i][j][k] = True
                
templist.append(temp)
zeroCount = 0

while templist :
    temp = []
    cnt += 1
    k = templist.popleft()
    for point in k :
        z,y,x = point
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and visited[nz][ny][nx] == False:
                if tomato[nz][ny][nx] == 0:
                    temp.append((nz,ny,nx))
                    tomato[nz][ny][nx] = 1
                    visited[nz][ny][nx] = True
    
    if len(temp) > 0:
        templist.append(temp)
    
flag = 1
for i in range(h):
    for x in tomato[i]:
        if x.count(0) > 0 :
            flag = 0

print("-1" if flag == 0 else cnt-1)
                
                
## 2차원으로 먼저 구현했으나 차원을 넘나드는 문제 때문에 3차원으로 변경
# from sys import stdin
# from collections import deque
# n, m, h = map(int, input().split())

# lst = [list(map(int, stdin.readline().rstrip().split())) for i in range(m*h)]
# # print(lst)

# cnt = 0
# templist = deque()
# temp = []

# zeroCount = 0
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# for i in range(m*h):
#     for j in range(n):
#         if lst[i][j] == 1:
#             temp.append((i, j))
    
# templist.append(temp)

# while templist :
#     temp = []
#     cnt += 1
#     k = templist.popleft()
#     for i in k:
#         x,y = i
#         px = x + m
#         mx = x - m
        
#         if 0 <= px < m*h:
#             if lst[px][y] == 0:
#                 lst[px][y] = 1
#                 temp.append((px,y))
#                 zeroCount -= 1
                
#         if 0 <= mx < m*h:
#             if lst[mx][y] == 0:
#                 lst[mx][y] = 1
#                 temp.append((mx,y))
#                 zeroCount -= 1
                
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             # print(x, y)

#             if 0 <= nx < m*h and 0 <= ny < n:
#                 if lst[nx][ny] == 0:
#                     lst[nx][ny] = 1
#                     zeroCount -= 1
#                     temp.append((nx, ny))
#                 else : # 여기도 생각 다시 해봐야됨
#                     continue
                
    
#     if len(temp) > 0:
#         templist.append(temp)
#     print(lst)


# flag = 1

# for x in lst:
#     if x.count(0) > 0 :
#         flag = 0

# print("-1" if flag == 0 else cnt-1)