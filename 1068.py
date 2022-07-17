from sys import stdin

n = int(input())
lst = list(map(int, stdin.readline().rstrip().split()))

removed = int(input())

    
def dfs(removed, lst):
    lst[removed] = -2 # -1은 루트랑 헷갈릴 수 있으므로 -2로 설정
    for i in range(len(lst)):
        if lst[i] == removed:
            dfs(i, lst)
            
cnt = 0 
dfs(removed, lst)
for i in range(len(lst)):
    if lst[i] != -2 and i not in lst:
        cnt += 1
print(cnt)