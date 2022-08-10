n = int(input())
target = int(input())

graph = []

for i in range(1,n+1):
    for j in range(1,n+1):
        graph.append(i*j)
        
print(graph)

print(sorted(graph)[target-1])