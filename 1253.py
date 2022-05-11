# 1. 모든 경우의 경우의 수로 도전
# 2. 
from sys import stdin
from itertools import combinations

n = int(input())

#숫자들 리스트
lst = sorted(list(map(int, stdin.readline().rstrip().split())))

possibleList = set()
#경우의 수 리스트
possible = list(combinations(lst, 2))
for x in possible:
    possibleList.add(sum(x))

possibleList = list(possibleList)

#범위 내에 있는 값만 추려논 possibleList 만들기 
while True:
    for i in range(len(possibleList)-1, 0 , -1):
        if possibleList[i] > lst[-1] :
            possibleList.pop()
        else :
            break
    break

print(possibleList)
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


cnt = 0
for x in lst:
    cnt += binary_search(x, possibleList)

print(cnt)