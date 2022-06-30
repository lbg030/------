number, bagWeight = map(int, input().split())


lst = [[0,0]] + [list(map(int, input().split())) for _ in range(number)]

knapsack = [ [0] * (bagWeight + 1) for _ in range(number + 1)]

for i in range(1, number+1):
    for j in range(1, bagWeight + 1):
        value, weight = lst[i][1], lst[i][0]
        
        if j < weight :
            knapsack[i][j] = knapsack[i-1][j]
        else :
            knapsack[i][j] = max(value + knapsack[i-1][j-weight], knapsack[i-1][j])

print(knapsack[number][bagWeight])