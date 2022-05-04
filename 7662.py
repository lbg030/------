from sys import stdin
import heapq

testCase = int(input())

for _ in range(testCase):
    cases = int(input())
    heapMin = []
    heapMax = []
    removed = [0] * cases
    for i in range(cases):
        a, b = input().split()
        # b가 str이기 때문에 int로 캐스팅
        b = int(b)

        if a == 'I':
            heapq.heappush(heapMin, (b, i))
            heapq.heappush(heapMax, (-b, i))

        elif a == 'D':
            # 최대값
            if b == 1:
                while heapMax:
                    # 만약 이미 삭제된 숫자면 제거
                    if removed[heapMax[0][1]] == 1:
                        heapq.heappop(heapMax)
                    else:
                        break
                if heapMax:
                    a = heapq.heappop(heapMax)[1]
                    removed[a] = 1

            if b == -1:
                while heapMin:
                    # 만약 이미 삭제된 숫자면 제거
                    if removed[heapMin[0][1]] == 1:
                        heapq.heappop(heapMin)
                    else:
                        break
                if heapMin:
                    a = heapq.heappop(heapMin)[1]
                    removed[a] = 1
    while heapMin:
        if removed[heapMin[0][1]] == 1:
            heapq.heappop(heapMin)
        else:
            break

    while heapMax:
        if removed[heapMax[0][1]] == 1:
            heapq.heappop(heapMax)
        else:
            break
    if heapMin:
        print(-heapMax[0][0], heapMin[0][0])
    else:
        print("EMPTY")
    # print(f"heapMin = {heapMin}, heapMax = {heapMax}")
