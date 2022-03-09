# 콤비네이션 하면 됨.

from sys import stdin
from itertools import combinations
import math


number = int(stdin.readline())

for i in range(number):
    n, m = map(int, stdin.readline().split())
    # print(f'n = {n} , m = {m}')
    it = int(math.factorial(m) / (math.factorial(n) * math.factorial(m-n)))
    print(it)
    # print(combinations(range(1, n), m))
# 콤비네이션으로 하면 더 느림
