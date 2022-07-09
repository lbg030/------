from sys import stdin

INF = float("inf") 


n,m = map(int, input().split())
timeMachine = [list(map(int, stdin.readline().rstrip().split() ))for _ in range(m)]
bellmanFordList = [INF] * (n+1)

def bellmanFord():
    bellmanFordList[1] = 0 # 출발 지점
    for i in range(1, n+1): #n번 반복 
        for j in range(m): # 총 n*m 반복 
            start,end,cost =  timeMachine[j][0], timeMachine[j][1], timeMachine[j][2]
                
            if bellmanFordList[start] != INF and bellmanFordList[end] > bellmanFordList[start] + cost:
                bellmanFordList[end] = bellmanFordList[start] + cost
                    
                if i == n:
                    return True
            
    return False

flag = bellmanFord()

if flag:
    print("-1")
else :
    for x in bellmanFordList[2:]:
        if x == INF:
            print("-1")
        else :
            print(x)