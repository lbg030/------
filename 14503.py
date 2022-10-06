#둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.

N, M = map(int, input().split())
robot = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

clean = 0
x ,y, direction = robot[0],robot[1],robot[2]

# 왼쪽으로 회전
def left_move(x,y,direction):
    if direction == 0:
        return x,y-1,3
    
    elif direction == 1:
        return x-1,y,0
    
    elif direction == 2:
        return x, y+1,1
    
    else :
        return x+1,y,2

def back(x,y,direction):
    if direction == 0:
        return x+1,y,direction
    
    elif direction == 1:
        return x,y-1,direction
    
    elif direction == 2:
        return x-1,y,direction
    
    else :
        return x,y+1,direction

def bounding_check(x,y, direction = None):
    if 0 <= x < N and 0 <= y < M :
        return True
    else :
        return False
    
def cleaning_check(x,y,direction = None):
    if graph[x][y] == 0 and visited[x][y] == False:
        return True
    else :
        return False
    
    return 
while True:
    # 청소할 상황이 있는 경우 
    print(x,y)
    
    clean += 1
    visited[x][y] = True
    temp_x,temp_y,temp_direction = left_move(x,y,direction)
    
    if bounding_check(temp_x,temp_y,direction) and cleaning_check(temp_x, temp_y, direction):
        x,y,direction = temp_x, temp_y, temp_direction

    else :
        num = 0
        while num < 4:
            if num == 1:
                temp_x, temp_y, temp_direction = left_move(x,y,direction)
            else :
                temp_x, temp_y, temp_direction = left_move(x,y,temp_direction)
            
            print(temp_x,temp_y, temp_direction)
            print(bounding_check(temp_x,temp_y,temp_direction), cleaning_check(temp_x, temp_y, temp_direction))
            
            if bounding_check(temp_x,temp_y,temp_direction) and cleaning_check(temp_x, temp_y, temp_direction):
                x,y,direction = temp_x, temp_y, temp_direction
                break
            
            num += 1
    
        else: # 주변에 청소가 다 되어있거나 벽이라는 뜻
            cnt = 0
            while bounding_check(temp_x,temp_y,direction):
                if cnt == 0:
                    temp_x,temp_y,temp_direction = back(x,y,direction)
                else :
                    temp_x,temp_y,temp_direction = back(temp_x,temp_y,temp_direction)
                    
                if bounding_check(temp_x,temp_y,temp_direction) and cleaning_check(temp_x, temp_y, temp_direction):
                    x,y,direction = temp_x, temp_y, temp_direction
                    break
                
                cnt += 1
            
            else :
                break
# 1번 상황 체크
print(clean)