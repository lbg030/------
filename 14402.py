from sys import stdin

q = int(input())
dic = {}
count = 0
for _ in range(q):
    info = list(stdin.readline().rstrip().split())
    name, data = info[0], info[1]

    if data == '-':
        if name not in dic or dic[name] == 0:  # 3
            count += 1
        elif name in dic:  # 2
            dic[name] -= 1

    else:  # 1
        if name not in dic:
            dic[name] = 1
        else:
            dic[name] += 1

# 야근하는 총 직원 수
if len(dic) == 0:
    print(count)
else:
    print(sum(dic.values()) + count)
