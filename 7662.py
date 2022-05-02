# heap과 우선순위 큐는 Mini구하기는 쉽지만 max 하는건 어렵다
# 우선순위 큐 두개를 사용해서 하나는 정상 하나는 -를 붙여서 최대 최소를 구한다.

import heapq
testCase = int(input())

for _ in range(testCase):
    lst = []
    case = int(input())

    # 케이스 개수 만큼 반복
    for _ in range(case):
      # n = I or D / m = 정수
        n, m = input().split()
        m = int(m)

        # insert
        if n == 'I':
            heapq.heappush(lst, m)

        # delete
        else:
            # -1일때 최소 / 1일때 최대
            if m == -1:
                if lst:
                    heapq.heappop(lst)
            else:
                if lst:
                    max_lst = [-x for x in lst]
                    heapq.heapify(max_lst)
                    heapq.heappop(max_lst)
                    lst = [-x for x in max_lst]
                    heapq.heapify(lst)
        print(lst, n, m)

    if not lst:
        print("Empty")
    else:
        print(lst[-1], lst[0])
