n = int(input())
m = int(input())
button = {str(i) for i in range(10)}
button1 = []

if m != 0:
    errorbuttons = list(map(str, input().split(" ")))
    for i in button:
        if i not in errorbuttons:
            button1.append(i)
else:
    button1 = button

minCount = abs(100 - n)

for num in range(1000001):
    num = str(num)

    for j in range(len(num)):
        if num[j] not in button1: # 어떤 수가 갱신된 button1에 없으면
            break # 번호 누르기 로는 이동 불가
    else : #
            minCount = min(minCount, abs(n - int(num)) + len(str(num)))

print(minCount)