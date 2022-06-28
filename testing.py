n = int(input())

lst = []
cnt = 0
tempCnt = 1
lst.append(int(input()))
for _ in range(n-1):
    x = lst.pop()
    lst.append(int(input()))
    if x * lst[-1] > 0:
        # print("1")
        tempCnt += 1
    else :
        cnt = max(cnt, tempCnt)
        tempCnt = 1
print(max(cnt, tempCnt))