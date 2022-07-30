from collections import deque
n, m = map(int, input().split())
ground = [list(map(int, list(input()))) for _ in range(n)]
# 0,0 출발 n-1, m-1 도착 벽 한번 부술 수 있음

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    q = deque()
    q.append((0,0,1,1))
    
    while q:
        x,y,cnt,availableBroken = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < n and 0<= ny < m:
                if ground[nx][ny] == 0:
                    ground[nx][ny] = [(cnt+1, availableBroken,False)]
                    q.append((nx,ny,cnt+1,availableBroken))
                
                #벽을 부순 경우
                elif ground[nx][ny] == 1 and availableBroken == 1:
                    ground[nx][ny] = [(cnt+1, availableBroken-1,True)]
                    q.append((nx,ny,cnt+1,availableBroken-1))
                    
                #1이지만 벽을 부술 수 없는 경우
                elif ground[nx][ny] == 1 and availableBroken == 0:
                    continue
                    
                #이미 (cnt,availableBroken, alreadyBroken)이 들어갔는데 다시 들어가 보는 경우
                else:
                    for lst in ground[nx][ny]:
                        
                    #벽을 부순 경우가 아닐경우
                        if lst[2] == False and availableBroken != lst[1]:
                            if cnt +1 < lst[0]:
                                        ground[nx][ny].append([cnt+1,availableBroken,False])
                                        q.append((nx,ny,cnt+1, availableBroken))
                                    
                            #벽을 부순 경우(1이였기 때문에 새로들어온 얘도 벽을 부술수 있어야함)
                        else :
                                #벽을 부술수 있는 경우
                                if availableBroken and lst[1] != availableBroken:
                                    if cnt + 1 < lst[0]:
                                        ground[nx][ny].append([cnt+1,availableBroken-1,True])
                                        q.append((nx,ny,cnt+1, availableBroken-1))

                                #벽을 부술수 없는 경우
                                else:
                                    continue
bfs()
print(ground)
if ground[-1][-1] == 0 :
    print("-1")
else :
    print(ground[-1][-1][0])