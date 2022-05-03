# heap과 우선순위 큐는 Mini구하기는 쉽지만 max 하는건 어렵다
# 우선순위 큐 두개를 사용해서 하나는 정상 하나는 -를 붙여서 최대 최소를 구한다.
# 동일 수 3개를 넣었을 때 heapify가 정상적으로 되지 않음
import sys
import heapq
case = int(input())
for _ in range(case):
    cases = int(input())
    # 최소 최대 리스트 생성
    maxList = []
    minList = []

    # 삭제가 되었는지 안되었는지 확인
    removed = [0]*cases
    for i in range(cases):
        a, b = sys.stdin.readline().split()

        if a == 'I':
          # 최대 힙에다가는 -값 넣어서 정렬되게 하고 최소힙에는 그대로 값 넣는다
          # i는 나중에 삭제되었는지 안되었는지 확인하기 위해 같이 넣는다.
            heapq.heappush(maxList, ((-1)*int(b), i))
            heapq.heappush(minList, (int(b), i))

        # 삭제
        # -1일때는 최소 값 / 1일 때는 최대 값
        elif a == 'D':

            # 최솟값
            if b == '-1':
                while minList:
                  # 만약 이미 제거된 문자열이 앞 존재한다면 전부 다 제거
                    if removed[minList[0][1]] == 1:
                        heapq.heappop(minList)
                    else:
                        break
                if minList:
                    # min은 i의 값을 가지고 와서 Remove[i]값을
                    # 이미 제거 되었다는 뜻으로 1로 변환 시킴
                    min = minList[0][1]
                    removed[min] = 1
                    heapq.heappop(minList)

            # 최대값
            elif b == '1':
                while maxList:
                  # 만약 이미 제거 된 문자열이 존재한다면 전부 다 제거
                    if removed[maxList[0][1]] == 1:
                        heapq.heappop(maxList)
                    else:
                        break
                if maxList:
                  # while문에서 제거된 문자열들은 제거되고 맨앞에 있는 숫자가
                  # 제일 큰 숫자이기 때문에 max설정하고
                    max = maxList[0][1]
                    removed[max] = 1
                    heapq.heappop(maxList)

    while maxList:
        if removed[maxList[0][1]] == 1:
            heapq.heappop(maxList)
        else:
            break
    while minList:
        if removed[minList[0][1]] == 1:
            heapq.heappop(minList)
        else:
            break
    if minList:
        print((-1)*maxList[0][0], minList[0][0])
    else:
        print("EMPTY")
