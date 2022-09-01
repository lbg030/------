N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

result = [0,0,0]

def dfs(x,y,graph):
    global result
    
    for i in range(x):
        if len(set(graph[i])) > 1:
            dfs(x//3, y//3, graph[:x//3][y//3])

def slice(x,y,n,graph):
    lst = []
    for i in range(x, x+n):
        lst.append(graph[i][y:y+3])
        
    return lst