n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

def dnc(x,y,n):
    k = graph[x][y]
    flag = True
    for i in range(x, x + n):
        for j in range(y, y+n):
            if k != graph[i][j]:
                flag = False
                break
            
    if not flag:
        n = n//2
        print("(", end ='')
        dnc(x,y, n)
        dnc(x, y+n, n)
        dnc(x+n, y, n)
        dnc(x+n,y+n, n)
        print(")", end='')
        
    elif k == 1:
        print('1', end ='')
    else :
        print("0", end='')
        
dnc(0,0,n)