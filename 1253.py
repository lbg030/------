# 1. 모든 경우의 경우의 수로 도전
# -> 두 값을 더하면 그 두값을 뺀 리스트를 만들어 그 안에 있는지 비교
# -> 처음부터 모든 경우의 수를 더하지 말고 하나씩 비교.
# -> 만약 되었다면 그 값은 비교 리스트에서 아웃.

# 처음 짠 코드에서 반례로 
#4
#3 3 2 1 존재
from sys import stdin
from itertools import combinations

n = int(input())

#숫자들 리스트
lst = sorted(list(map(int, stdin.readline().rstrip().split())))
# print(lst)
realList = lst[:]
cnt = 0 
#이분 탐색 알고리즘
def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return 1 # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return 0

#길이가 3미만이라면 성립 불가
if len(lst) < 3:
    print("0")

else:
    for i in range(n):
        for j in range(i+1,n):
            #비교 리스트 초기화
            compareList = lst[:]

            # 더한 값
            m = lst[i] + lst[j]

            del compareList[i]
            del compareList[j-1]
            # print(compareList)
            a = binary_search(m, compareList)
            if a == 1 and m in realList:
                a = realList.count(m)
                cnt += a
                for _ in range(a):
                    realList.remove(m)
            # print(realList)
    print(cnt)