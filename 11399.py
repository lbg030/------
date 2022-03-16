n = int(input())

li = sorted(list(map(int, input().split())))

total = 0
for i in range(n):
    total += sum(li[:i+1])

print(total)
