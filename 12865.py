number, bagWeight = map(int, input().split())


lst = [[0,0]] + [list(map(int, input().split())) for _ in range(number)]

knapsack = [ [0] * (bagWeight + 1) for _ in range(number + 1)]

for i in range(1, number+1):
    for j in range(1, bagWeight + 1):
        