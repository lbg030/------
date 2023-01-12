from sys import stdin

def dfs(initial, connected_list, visited):
    
    for i in range(n):
        if not visited[initial]:
            visited[initial] = True
            if graph[initial][i] == connected_list[0] : # 처음과 연결되었다면
                return connected_list
            
            else :
                connected_list.append(i)
                # print(connected_list, i)
                dfs(i, connected_list, visited)
                
        #이미 팀이 구성된 얘들
        else :
            break

#Init
num_test = int(input())

#Test Case
for _ in range(num_test):
    n = int(input())
    graph = [[False] * (n) for _ in range(n)]
    lst = list(map(int, stdin.readline().strip().split()))
    visited = [False] * n
    results = []
    cnt = 0
    
    # graph
    for idx, num in enumerate(lst):
        graph[idx][num-1] = True
    
    #graph 탐색 dfs로 진행
    for i in range(n):
        if visited[i] == True: #만약 이미 완성된 얘라면 pass
            continue 
        else :
            temp_visited = visited[:]
            connected_list = dfs(i , [i], temp_visited)
            
            if connected_list:
                for num in connected_list:
                    visited[num] = True
                print(f"Connected_list = {connected_list}")
                results.append(connected_list)
                cnt += 1

    exit() # 한번만 해보게