from sys import stdin

n,m = map(int, input().split())

lst = [list(map(int, stdin.readline().rstrip().split())) for i in range(m)]

#안되는 경우 cnt로 판별
cnt = 0

templist = []

for i in range(m):
    for j in range(n):
        if lst[i][j] == 1 :
            templist.append((i,j))
            

print(templist)