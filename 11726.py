n = int(input())

li = [1, 2, 3, 5]

for i in range(4, n):
    li.append(li[i-2] + li[i-1])

print(li[n-1] % 10007)
# print(li)
