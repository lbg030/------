# 수학식 질문 찾다보면 나오지만
# 옷 2 머리 1 바지 5
# 옷(2+1) * 머리(1+1) * 바지(5+1) - 1
# 요고가 정답 (2+1) * (1+1) * (5+1) -1

## from collections import counter 을 이용하는게 훨씬 효과적.
#처음 풀이
def solution(clothes):
    answer = 1
    dic = {}
    categoryList = []
    for name, category in clothes:
        if category not in categoryList:
            dic[category] = [name]
            categoryList.append(category)
        else :
            dic[category].append(name)
        
    for x in categoryList:
        answer *= len(dic[x]) + 1
    answer -= 1
    return answer

#2번째 풀이
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    print(cnt)
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer