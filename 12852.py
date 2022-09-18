from collections import deque

def bfs(number, res_lst):
    q = deque()
    q.append((number, res_lst))
    
    while q:
        number, res_lst = q.popleft()
        # print(number, res_lst)
        for n in [number+1, number*2, number*3]:
            if n <= N and lst[n] == 0:
                if n == N:
                    return lst[number]+1, res_lst+[n]
                
                q.append((n, res_lst+[n]))
                lst[n] = lst[number]+1

N = int(input())
if N == 1:
    print(0)
    print(1)
else:
    lst = [0]*(N+1)
    
    cnt, res_lst = bfs(1, [1])
    print(cnt)
    print(*res_lst[::-1])