
def solution(n):
    # n이 제곱근이 정수라면 답은 1
    if int(n**0.5) == n**0.5:
        return 1
    # 1 ~ (n의 제곱근의 올림값)을 i라고 하고 (n - i^2)의 제곱근이 정수라면 답은 2
    for i in range(1, int(n**0.5) + 1):
        if int((n - i**2)**0.5) == (n - i**2)**0.5:
            return 2
    # (n - i^2 - j^2)의 제곱근이 정수라면 답은 3
    for i in range(1, int(n**0.5) + 1):
        for j in range(1, int((n - i**2)**0.5) + 1):
            if int((n - i**2 - j**2)**0.5) == (n - i**2 - j**2)**0.5:
                return 3
    # 1, 2, 3도 아닌경우 답은 4
    return 4


n = int(input())
print(solution(n))
