from collections import deque
n,m,s = map(int, input().split())

graph = [list(input()) for _ in range(n)]
target = input()
alpha_dic = {}

res = ''
cnt = 0

for x in target:
    for i in range(n):
        for j in range(m):
            if graph[i][j] == x:
                if x in alpha_dic:
                    alpha_dic[x].append([i, j])
                else :
                    alpha_dic[x] = deque()
                    alpha_dic[x].append([i, j])
                    
x,y = alpha_dic['c'].popleft()

print(x,y,type(x))