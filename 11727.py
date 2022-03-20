n = int(input())

li = [0, 1, 3, 5]

for i in range(4, n+1):
    li.append(li[i-1] + li[i-2] * 2)

print(li[n] % 10007)
