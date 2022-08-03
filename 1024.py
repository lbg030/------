N,L = map(int,input().split())

x=-1
y=-1
for i in range(L,101):
    t = (i-1)*i//2
    if ((N-t)%i == 0) & ((N-t)//i>=0):
        x = (N-t)//i
        y = i
        break
if x==-1:
    print(-1)
else:
    for i in range(0,y):
        print(x+i,end = " ")