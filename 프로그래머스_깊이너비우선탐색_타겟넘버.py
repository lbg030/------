# numbers	target	return
# [1, 1, 1, 1, 1]	3	5
# [4, 1, 2, 1]	4	2

#다 더해나가기
#number = [1,1,1,1,1] target = 3
#더하기 빼기로 dfs 생성
def solution(numbers, target):
    answer = 0
    a = numbers.pop()
    lst = [[a, -a]]
    while numbers:
        #숫자 하나 빼기
        a = numbers.pop()
        tempList=[]
        #점점 가지 수 늘려나가기 DFS
        for i in range(len(lst[-1])):
            tempList.append([lst[-1][i] + a, lst[-1][i] - a])
        lst.append(sum(tempList, []))
    for x in lst[-1]:
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