def solution(food_times, k):
    answer = 0
    i = 0
    count = 0
    while sum(food_times) > 0:
        # 0이 아니면 -1씩 빼기
        if(food_times[i] != 0):
            food_times[i] -= 1
        # k와 비교하기 위한 count, 인덱스 i 추가
        i += 1
        count += 1

        # 만약 i가 끝에 도달하면 다시 0으로 초기화
        if(i > len(food_times) - 1):
            i = 0

         # 이쪽 문제일 확률 100%
        if(count == k):
            answer = i+2  # 4~5초가 아니라 5~6초가 오류나는 거기 때문에 2를 더해야됨

            # 만약에 답의 인덱스가 len을 초과하게 된다면
            if(answer > len(food_times)):
                answer = answer % (len(food_times)-1)
            break
    if(sum(food_times) == 0):
        anwer = -1
    print(answer)
    return answer


print(solution([3, 1, 2], 5))
