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
                    alpha_dic[x].append((i, j))
                else :
                    alpha_dic[x] = deque()
                    alpha_dic[x].append([i, j])
                    
def direction(x,y,final = False):
    ans = ''
    if x < 0: # go_x < x
        ans += 'U' * abs(x)
    else :
        ans += 'D' * abs(x)
        
    if y < 0: # go_y < y
        ans += 'L' * abs(y)
    else :
        ans += 'R' * abs(y)
    
    if not final:
        ans += 'P'
    
    return ans

x, y = 0,0

while True :
    temp_res = ''
    for alpha in target:
        if alpha_dic[alpha]:
            go_x, go_y = alpha_dic[alpha].popleft()
            # print(type(temp_res),type(x),type(go_x))
            temp_res += direction(go_x - x, go_y - y)
            x,y = go_x,go_y
            flag = True
            
        else :
            flag = False
            break
        
    if flag :
        res += temp_res
        final_x,final_y = x,y
        cnt += 1
        
    else :
        res += direction(n-x-1, m-y-1, True)
        break

print(cnt, len(res))
print(res)
