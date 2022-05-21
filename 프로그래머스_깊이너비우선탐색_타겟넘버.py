# numbers	target	return
# [1, 1, 1, 1, 1]	3	5
# [4, 1, 2, 1]	4	2

#다 더해나가기
#number = [1,1,1,1,1] target = 3
#더하기 빼기로 dfs 생성
def solution(numbers, target):
    from collections import deque
    answer = 0
    a = numbers.pop()
    lst = deque([a, -a])
    while numbers:
        #숫자 하나 빼기
        a = numbers.pop()
        tempList=[]
        summation = sum(numbers)
        #점점 가지 수 늘려나가기 DFS
        for i in range(len(lst)):
            #더하거나 빼거나 하는 경우 2가지를 정의
            plus, minus = lst[i] + a, lst[i] - a
            # 3, -1 summation = 5, target = 4
            if(plus > target and plus - summation > target):
                if(minus + summation >= target):
                    tempList.append([minus])
            else:
                if(minus + summation >= target):
                    tempList.append([plus,minus])
                else :
                    tempList.append([plus])
        if tempList:
            lst = deque(sum(tempList, []))
            print(lst)
    # print(lst)
    for x in lst:
        if x == target:
            answer += 1
    return answer

k = list(map(int, input().split()))
n = int(input())

# print(k,n)
lst = solution(k,n)
print(lst)
# cnt = 0
# for x in lst[-1] :
#         if x == n:
#             cnt += 1
            
# print(cnt)