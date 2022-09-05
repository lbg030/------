n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

res = [0,0,0] # 0 , 1 , -1 개수

def dnc(x,y,n):
    k = graph[x][y]
    flag = True
    
    for i in range(x, x + n):
        for j in range(y, y+n):
            if n != 1:
                if k != graph[i][j]:
                    flag = False
                    break
            else :
                # print(graph[i][j],"res = ",res)
                res[graph[i][j]] += 1
                
            
    if not flag :
        # print()
        # print(x,y,n)
        # print(res)
        
        n = n//3
        dnc(x,y,n) # 왼쪽 위
        dnc(x, y+n, n) # 맨위 중간
        dnc(x, y+(2*n),n) # 맨위 오른쪽
        
        dnc(x+n, y, n) #중간 왼쪽
        dnc(x+n, y+n, n) #중간 가운데
        dnc(x+n, y+(2*n),n) #중간 오른쪽
        
        dnc(x+2*n, y,n) #맨 아래 왼쪽
        dnc(x+2*n,y+n, n) # 맨 아래 중간
        dnc(x + 2*n, y+2*n,n)
        
    else :
        # print(k)
        if n != 1:
            res[k] += 1

        
dnc(0,0,n)
print(res[-1])
print(res[0])
print(res[1])