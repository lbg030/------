# 1016번 제곱 ㄴㄴ수

# main
minNum, maxNum = map(int, input().split())

eratos = [False for _ in range(maxNum-minNum+2)]

cnt = maxNum - minNum + 1
i = 2
while i**2 <= maxNum:
    s = minNum // (i**2)
    if minNum % (i**2) != 0:
        s += 1

    while s*(i**2) <= maxNum:
        if not eratos[s*(i**2) - minNum]:
            eratos[s*(i**2) - minNum] = True
            cnt -= 1
        s += 1
    i += 1

print(cnt)
