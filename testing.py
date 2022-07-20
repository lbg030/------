n,t = map(int, input().split())

x,y,c=input().split()
x,y = int(x), int(y)

d = {'U':0, 'R': 1, 'D':2, 'L':3}

dx = [-1,0,1,0]
dy = [0,1,0,-1]

d_num = d[c]

for _ in range(t):
    if 1<= x <= n or 1 <= y <= n:
        x = x + dx[d_num]
        y = y + dy[d_num]

    else :
        d_num = (d_num + 2) % 4
        x = x + dx[d_num]
        y = y + dy[d_num]
        
    print(x,y)
# print(x,y)