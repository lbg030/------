n = int(input())

li = [300, 60, 10]
res = []
# 나누어 떨어지지 않는 경우
if(n % li[2] != 0):
    print("-1")
else:
    i = 0
    while i < 3:
        res.append(n // li[i])
        n = n % li[i]
        i += 1

    print(*res)
