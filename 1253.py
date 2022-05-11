# 1. 모든 경우의 경우의 수로 도전
# -> 두 값을 더하면 그 두값을 뺀 리스트를 만들어 그 안에 있는지 비교
# -> 처음부터 모든 경우의 수를 더하지 말고 하나씩 비교.
# -> 만약 되었다면 그 값은 비교 리스트에서 아웃.
from sys import stdin
from itertools import combinations

n = int(input())

#숫자들 리스트
lst = sorted(list(map(int, stdin.readline().rstrip().split())))




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
