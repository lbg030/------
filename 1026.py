n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
sum = 0
# print(f"a = {a},\n b = {b}")
for i in range(n):
    sum += (a[i] * b[i])
print(sum)
