n = int(input())

li = [0, 1, 1]

for i in range(3, n+1):
    li.append(int(li[i-2] + li[i-1]))

print(li[-1])
