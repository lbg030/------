# 설탕 문제
# 어찌 됐건 5로 나눠지는게 무조건 빠르기 때문에 -3씩 하다가 5로 나눠지면 계산
# 만약 3씩 빼다가 3보다 작아지는 상황이 되면 나누어 질 수 없는 것이기 때문에 -1 출력
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
