#0은 빈 칸을, 1은 / 모양을, 2는 \ 모양을 의미합니다.

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

# print(graph)
maxSecond = [[0] * n for _ in range(n)]
direction = {'down' : [0,1], "up" : [0,-1], "right": [1,0], "left": [-1,0]}

def up(x,y):
    while True:

def left(x,y):
    while True:

def right(x,y):
    while True:

def down(x,y,cnt):
    locating = 'down'
    directing = direction[locating]
    while True:
        dx, dy = directing[0], directing[1]
        x = x + dx 
        y = y + dy
        
        if x >= n or y >= n:
            break
    
    return cnt

def direct(n, directing):
    if n == 1:
        if directing == 'down':
            locating = 'left'
            
        if directing == 'up':
            locating = 'right'
        
        if directing == 'left':
            locating = 'down'
        if directing == 'right':
            locating = 'up'
    else :
        if directing =='down':
            locating = 'right'
        if directing == 'up':
            locating = 'left'
        if directing == 'right':
            locating = 'down'
        if directing == 'left':
            locating = 'up'
    return locating
        
for i in range(n):
    for j in range(n):
        #0,0 혹은 오른위쪽은 방향이 두개이므로 두개 다 체크
        if i == 0 and j == 0:
            maxSecond[i][j] = max(down(i,j), right(i,j))
             
        elif i == 0 and j == n-1:
            maxSecond[i][j] = max(down(i,j), left(i,j))
        
        elif i == n-1 and j == 0:
            maxSecond[i][j] = max(up(i,j), right(i,j))
            
        elif i == n-1 and j == n-1:
            maxSecond[i][j] = max(up(i,j), left(i,j))
            
        else:
            