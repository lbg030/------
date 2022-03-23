# 1 - > 1
# 2 -> 1
# 3 -> 2
# 4 - > 3
# 5 -> 5

n = int(input())
li = [1, 1]

for i in range(2, n):
    li.append(li[i-2] + li[i-1])

print(li[-1])
