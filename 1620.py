# n, m = map(int, input().split())

# li = []
# for i in range(n):
#     li.append(input())

# # print(li)

# while m != 0:
#     temp = input()
#     if(ord(temp[0]) < 60):
#         print(li[int(temp)-1])
#     else:
#         print(li.index(temp)+1)
#     m -= 1
from sys import stdin

n, m = map(int, input().split())

dict = {}
for i in range(1, n+1):
    temp = stdin.readline().rstrip()
    dict[i] = temp
    dict[temp] = i

for j in range(m):
    question = stdin.readline().rstrip()
    if(question.isdigit()):
        print(dict[int(question)])
    else:
        print(dict[question])
