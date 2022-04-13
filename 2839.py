n = int(input())
cnt = 0
check = 0
while n >= 0:
    if n % 5 == 0:
        cnt += n // 5
        break

    n -= 3
    cnt += 1
    if(0 < n < 3):
        check = 1
        break

if(check == 1):
    print(-1)
else:
    print(cnt)
