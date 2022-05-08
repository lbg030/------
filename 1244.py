switch_num = int(input())  # 스위치 개수
switch_status = list(map(int, input().split()))  # 스위치 상태
student_count = int(input())  # 학생수
student_status = []  # 학생 성별과 받은 스위치 값 저장
for i in range(student_count):
    student_status.append(list(map(int, input().split())))

for i in student_status:

    if i[0] == 1:  # 남자일때
        for j in range(len(switch_status)):
            if (j + 1) % i[1] == 0:  # 스위치의 인덱스 + 1 값이 학생이 받은 스위치의 번호와 같다면
                # 그 값을 반대로 뒤집어 준다.
                switch_status[j] = int(not switch_status[j])
    else:  # 여자일때
        for j in range(len(switch_status)):
            if (j + 1) == i[1]:  # 스위치의 인덱스 + 1 값이 학생이 받은 스위치의 번호와 같다면
                plus = j + 1  # 그 다음 인덱스 저장
                minus = j - 1  # 그 전 인덱스 저장
                # 우선 해당 인덱스의 스위치 값을 반대로
                switch_status[j] = int(not switch_status[j])
                while True:

                    # 만약 범위를 벗어나지 않는다면
                    if minus >= 0 and plus < len(switch_status):
                        if switch_status[minus] == switch_status[plus]:  # 만약 양쪽이 대칭이라면
                            switch_status[minus] = int(
                                not switch_status[minus])  # 스위치 값을 반대로
                            switch_status[plus] = int(
                                not switch_status[plus])  # 스위치 값을 반대로
                        else:  # 대칭이 아니라면
                            break  # 더돌 필요가 없으므로 break
                    else:  # 만약 범위를 벗어난다면
                        break  # 바로 탈출

                    minus -= 1  # 왼쪽 인덱스는 한칸더 왼쪽으로
                    plus += 1  # 오른쪽 인덱스는 한칸더 오른쪽으로

count = 0  # 20개 출력을 위한 변수 선언
while count < len(switch_status):

    print(switch_status[count], end=" ")
    if count % 20 == 19:
        print()
    count += 1
