n = int(input())
subway = {}
for i in range(1,n+1):
    subway[i] = list(map(int, input().split()))[1:]
destination = int(input())

print(subway, destination)