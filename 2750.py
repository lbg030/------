from sys import stdin

n = int(input())

li = [int(stdin.readline().rstrip('\n')) for _ in range(n)]

# print(li)
for i in range(n):
    for j in range(n):
        if(li[i] < li[j]):
            li[i], li[j] = li[j], li[i]

for x in li:
    print(x)
