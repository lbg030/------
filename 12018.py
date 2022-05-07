subjectCase, mileage = map(int, input().split())
print("1")
lst = []
answer = 0
for _ in range(subjectCase):
    #지원자, 가능자
    application, possible = map(int, input().split())
    # 지원자 마일리지 리스트
    applicationList = sorted(list(map(int, input().split())), reverse=True)

    if application >= possible:
        minimumMileage = applicationList[possible-1]
        lst.append(minimumMileage)
    else:
        lst.append(1)

lst = sorted(lst)
# print(lst)
for x in lst:
    if mileage - x < 0:
        break
    else:
        mileage = mileage - x
        answer += 1

print(answer)
