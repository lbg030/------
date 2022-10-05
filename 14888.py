n = int(input())
number_list = list(map(int, input().split()))
operation = list(map(int, input().split())) # + - * /

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus,minus,multiple, divide):
    global maximum
    global minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    
    if plus:
        dfs(depth + 1, total + number_list[depth], plus - 1, minus, multiple, divide)
    if minus:
        dfs(depth + 1, total - number_list[depth], plus, minus - 1, multiple, divide)
    if multiple:
        dfs(depth + 1, total * number_list[depth], plus, minus, multiple - 1, divide)
    if divide:
        dfs(depth + 1, int(total / number_list[depth]), plus, minus, multiple, divide - 1)
   
        

dfs(1, number_list[0],operation[0], operation[1], operation[2], operation[3])

print(maximum)
print(minimum)