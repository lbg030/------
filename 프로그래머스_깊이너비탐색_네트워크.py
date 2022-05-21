#DFS 문제
def solution(n, computers):
    answer = 0
    def dfs(start):
        for i in range(len(computers[0])):
            if computers[start][i] == 1:
                computers[start][i] = computers[i][start] = 0
                dfs(i)
    dfs(0)
    answer += 1
    print(computers)
    for x in computers:
        answer += sum(x)
    return answer 


a = solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])
b = solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])
c = solution(3,[[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(solution(4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
print(a)
print(b)
print(c)
# print(d)