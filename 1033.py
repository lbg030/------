from math import gcd

n = int(input())
result = [1]*n
graph = {}

def gcd_list(lst):
    divided = lst[0]
    for x in lst:
        divided = gcd(divided, x)
    return divided

def dfs(a, b, edge):
    global visited
    
    # 이미 한 것이라면 pass
    if (a, edge) in visited: 
        return
    
    # pass가 안됐으면 아직 값 업데이트가 되지 않은 것.
    visited[(a, edge)] = True
    result[a] *= edge
    
    for x in graph[a]:
        if x != b: 
            dfs(x, a, edge)


cocktail_list=[]

for _ in range(n-1):
    a, b, p, q = map(int, input().split())
    
    if a not in graph:
        graph[a] = [b]
    else :
        graph[a].append(b)
        
    if b not in graph:
        graph[b] = [a]
    else :
        graph[b].append(a)
        
    cocktail_list.append((a, b, p, q))

for a,b,p,q in cocktail_list:
    visited={}
    dfs(a, b, p)
    dfs(b, a, q)
    # print(visited)
divided = gcd_list(result)
result = list(map(lambda x: x // divided , result))

print(*result)