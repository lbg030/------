from sys import stdin

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
            connected_list, flag = dfs(i, [], temp_visited)
            print(connected_list, flag)
            
            if connected_list and flag:
                for num in connected_list:
                    visited[num] = True
                print(f"Connected_list = {connected_list}")
                results.append(connected_list)
                cnt += 1
            
            else :
                visited[connected_list[0]] = True
            
            # else :
            #     print(connected_list)
    print(visited)
    exit() # 한번만 해보게