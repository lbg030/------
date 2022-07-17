# 이진 탐색 ( 조건의 크기가 크므로 , 시간 복잡도 생각해서 )
# 빠른 탐색을 위해 -> 문자열 길이에 따라 단어 저장
# 이진 탐색을 위한 정렬 ( 일반 정렬 , 역순 정렬 )
# 해당 단어 갯수 세는데 적절한 라이브러리 ' bisect 라이브러리 사용 '
# bisect 라이브러리 공부 참고 https://velog.io/@ssongplay/Python-bisect-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC

from bisect import bisect_left, bisect_right

def count_by_range(arr, left_value, right_value):
    left_index = bisect_left(arr, left_value)
    right_index = bisect_right(arr, right_value)
    return right_index - left_index

def solution(words, queries) :
    answer = [] # 단어 길이 순으로 분리하기 위해서 딕셔너리 생성
    arr = [[] for _ in range(10001)]
    reversed_arr = [[] for _ in range(10001)]
    # 단어 길이 순으로 분리
    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])
    # 정렬 시키기
    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()

    # 쿼리 하나씩 확인하며
    for query in queries:
        # 접두사에 와일드 카드 붙은 경우
        if query[0] == '?':
            cnt = count_by_range(reversed_arr[len(query)],query.replace('?','a')[::-1], query.replace('?','z')[::-1])
        # 접미사에 와일드 카드 붙은 경우
        else:
            cnt = count_by_range(arr[len(query)], query.replace('?','a'),query.replace('?','z'))
        answer.append(cnt)
    return answer