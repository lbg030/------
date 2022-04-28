# start, finish 라인 쪽 input().split()으로 하면 시간 초과 남.
# stdin.readline()으로 해도 마찬가지

# [1,2,3,4,5]
#sum = 15
# 7이 나오려면 10 - 3
# prefix sum이라는 개념을 사용
# 미리 값을 저장한 리스트를 만들어두고 사용 만약 L,R까지의 합을 구하려면
# sumlst[R] - sumlst[L]
from sys import stdin

number, case = map(int, input().split())

lst = list(map(int, input().split()))
prefixSum = [0]

for i in lst:
    prefixSum.append(prefixSum[-1] + i)

# print(prefixSum)
for _ in range(case):
    start, finish = map(int, stdin.readline().rstrip().split())
    result = prefixSum[finish] - prefixSum[start - 1]
    print(result)
