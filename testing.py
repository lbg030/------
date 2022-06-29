
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

if len(aList) < len(bList):
    aList.extend(([aList[-1]] * (len(bList) - len(aList))))
else :
    bList.extend(([bList[-1]] * (len(aList) - len(bList))))
    
a,b = 0,0            
cnt = 0
maximum = max(len(aList), len(bList))

if aList[0] == bList[0] :
    cnt += 1

# second = 2
if maximum > 1:
    for i in range(1, maximum):
        # second += 1
        
        aTemp = aList[i-1]
        a = aList[i]
        bTemp = bList[i-1]
        b = bList[i]

        if a == b and (aTemp != bTemp):
            cnt += 1
            
        # print(second)

print(cnt)
# print(aList)
# print(bList)