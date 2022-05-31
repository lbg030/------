from collections import deque


n = int(input())

Cowgraph = [list(input()) for _ in range(n)]
notCowgraph = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]
#G -> R로 변경
for x in Cowgraph:
    tempList = []
    for k in x:
        temp = k.replace("G","R")
        tempList.append(temp)
    notCowgraph.append(tempList)
cowvisited = [[False] * n for _ in range(n)]
notCowvisited = [[False] * n for _ in range(n)]

Cowcnt = 0
notCowCnt = 0
#Cowart = 적록색약
#notCowart = 적록색약 아님

def notCowArt(x,y):
    queue = deque()
    queue.append((x,y))
    # notCowvisited[x][y] == True
    while queue:
        notCowvisited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
                
            if nx < 0 or ny < 0 or nx >= n or ny >= n :
                    continue
            
            if Cowgraph[nx][ny] == Cowgraph[x][y] and cowvisited[nx][ny] == False:
                cowvisited[nx][ny] = True
                queue.append((nx,ny))
    return 

def cowArt(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        notCowgraph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
                
            if nx < 0 or ny < 0 or nx >= n or ny >= n :
                    continue
            
            if notCowgraph[nx][ny] == notCowgraph[x][y] and notCowvisited[nx][ny] == False:
                notCowgraph[nx][ny] = 0
                queue.append((nx,ny))
    return 

for x in range(n):
    for y in range(n):
        if y+1 < n :
            if Cowgraph[x][y] == Cowgraph[x][y+1]:
                cowArt(x,y) 
                Cowcnt +=  1
            elif notCowgraph[x][y] == notCowgraph[x][y+1]:
                notCowArt(x,y)
                notCowCnt += 1  
        if x+1 < n:
            if Cowgraph[x][y] == Cowgraph[x+1][y]:
                cowArt(x,y)
                Cowcnt += 1
            if notCowgraph[x][y] == notCowgraph[x+1][y]:
                notCowArt(x,y)
                notCowCnt += 1

print(Cowcnt, notCowCnt)