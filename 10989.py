from sys import stdin
from collections import deque
n = int(input())

li = [int(stdin.readline().rstrip('\n')) for _ in range(n)]


def quick_sort(array):
    # 리스트가 하나 이하의 원소를 가지면 종료
    if len(array) <= 1:
        return array

    pivot, tail = array[0], array[1:]

    leftSide = [x for x in tail if x <= pivot]
    rightSide = [x for x in tail if x > pivot]

    return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)


a = quick_sort(li)
print(a)
