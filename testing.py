from collections import Counter
from functools import reduce

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    print(cnt)
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    print(answer)
    return answer

print(solution(clothes))