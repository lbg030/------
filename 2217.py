from sys import stdin

n = int(input())
li = []
for _ in range(n):
    li.append(int(stdin.readline().rstrip()))

li.sort(reverse=True)
result = 0
# print(li)
for i in range(0, n):
    result = max(result, li[i]*(i+1))

print(result)
# 27 26 25 가 존재
# 27, 26.5, 25.5
