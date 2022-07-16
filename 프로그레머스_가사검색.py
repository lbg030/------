from collections import defaultdict
from bisect import bisect_left, bisect_right

word= ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]



def solution(words, queries):
    answer = []
    d = defaultdict(list) # 구현을 편하게 해준다. 모른다면 찾아보면 좋다.
    r_d = defaultdict(list)
    for word in words:
        d[len(word)].append(word) # 길이 별로 저장
        r_d[len(word)].append(word[::-1]) # 순서를 뒤집은 배열
    for k in d.keys():
        d[k].sort() # 이진 탐색을 위해 sort
        r_d[k].sort() 
        
    for query in queries:
        n = len(query)
        cnt = 0
        e_query = query.replace('?', 'z')
        # print(e_query)
        # print(r_d)
        if query == '?'*n:
            cnt += len(d[n])
        
        #접두사일때는 뒤집어서 search
        elif query[0] == '?':
            query, e_query = query[::-1], e_query[::-1]
            l, r = bisect_left(r_d[n], query), bisect_left(r_d[n], e_query)
            print(l,r)
            cnt += r-l
        else:
            l, r = bisect_left(d[n], query), bisect_left(d[n], e_query)
            cnt += r-l

        answer.append(cnt)
            
    return answer

print(solution(word, queries))