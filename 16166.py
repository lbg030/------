#출발역은 항상 0 번째
#BFS로 해결해야 될 것 같음

n = int(input())
subway = {}
for i in range(1,n+1):
    subway[i] = list(map(int, input().split()))[1:]
destination = int(input())

print(subway, destination)

def BFS(start, final):
    pass