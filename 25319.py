n,m,s = map(int, input().split())

graph = [list(input()) for _ in range(n)]
target = input()
x, y = 0,0
res = ''
cnt = 0
final_res = ''
reserve_x, reserve_y = 0,0
flag = True

def left_or_right(lst, alpha, y):
    ans = ''
    value = lst.index(alpha) - y 
    if value < 0 :
        ans += 'L' * abs(value)
    
    else :
        ans += 'R' * abs(value)
    
    ans += 'P'
    return ans


while flag:
    res = ''
    for alpha in target:
        flag = False
        
        if alpha in graph[x]:
            y = graph[x].index(alpha)
            res += left_or_right(graph[x], alpha, y)
            graph[x][y] = '.'
            flag = True
            
        else:
            for i in range(1, max(n-x, x)):
                plus = x + i
                minus = x - i
                
                # x보다 밑에 있음
                if plus < n:
                    if alpha in graph[plus]:
                        res += 'D' * (plus - x)
                        res += left_or_right(graph[plus], alpha, y)
                        
                        x = plus
                        y = graph[plus].index(alpha)
                        graph[x][y] = '.'
                        flag = True
                        continue
                    
                elif 0 < minus :
                    if alpha in graph[minus]:
                        res += 'U' * (x - minus)
                        res += left_or_right(graph[minus], alpha, y)
                            
                        x = minus
                        y = graph[minus].index(alpha)
                        graph[x][y] = '.'
                        res += 'P'
                        flag = True
                        continue
                    
            if not flag:
                break
        
    if flag:
        final_res += res
        cnt += 1
        reserve_x = x
        reserve_y = y
        
    else :
        # print(final_res, x,y)
        final_x = n - reserve_x - 1
        final_y = m - reserve_y - 1
        
        final_res += 'D' * final_x
        final_res += 'R' * final_y
        # print(final_res)
        
print(cnt,len(final_res))
print(final_res)