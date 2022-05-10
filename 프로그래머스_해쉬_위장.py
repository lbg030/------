def solution(clothes):
    answer = 0
    dic = {}
    categoryList = []
    for name, category in clothes:
        if category not in categoryList:
            dic[name] = [name]
            categoryList.append(category)
        else :
            dic[category].append(name)
    return answer



clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)