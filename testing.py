#1초에 1m씩 이동한다.
n, m = map(int, input().split())
aList = []
bList = []

aDistance = 0
bDistance = 0
for _ in range(n):
    b,a = input().split()
    
    b = int(b)
    if a == "R":
        for _ in range(b):
            aDistance += 1
            aList.append(aDistance)
    else :
        for _ in range(b):
            aDistance -= 1
            aList.append(aDistance)
    
for _ in range(m):
    b,a = input().split()
    b = int(b)
    if a == "R":
        for _ in range(b):
            bDistance += 1
            bList.append(bDistance)
    else :
        for _ in range(b):
            bDistance -= 1
            bList.append(bDistance)
flag = -1
for i in range(len(aList)):
    if aList[i] == bList[i]:
        flag = i+1
        break

print(flag)