import ast

dot1 = ast.literal_eval(input())
dot2 = ast.literal_eval(input())
dot3 = ast.literal_eval(input())
dot4 = ast.literal_eval(input())

lst = [dot1,dot2,dot3,dot4]
print(lst)
lst = sorted(lst, key = lambda x : x[1])

print(lst)

x = sum(lst[i][0] for i in range(4)) / 4
y = sum(lst[i][1] for i in range(4)) / 4

x = lst[-1][0] - lst[0][0]
y = lst[-1][1] - lst[0][1]

gradient = y/x