from sys import stdin
n, m = map(int, input().split())
li = [list(map(str, stdin.readline().rstrip())) for i in range(n)]
# print(li[1])
cnt = 0
for i in range(n-1):
    for j in range(m-1):
        if(li[i][j] == '|' and li[i+1][j] == '|'):
            cnt += 1
            li[i][j] = ''
            li[i+1][j] = ''
        elif(li[i][j] == '-' and li[i][j+1] == '-'):
            cnt += 1
            li[i][j] = ''
            li[i][j+1] = ''

print(li)
print(cnt)
