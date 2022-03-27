li = list(input())
result = 0
lst = []

for i in range(len(li)):
    if(li[i] == '('):
        lst.append('(')

    else:
        if li[i-1] == '(':  # ')'로 닫혔을 때 만약 앞에가 '(' 라면

            lst.pop()  # 일단 닫아주고 앞에 열린만큼 더해주기
            result += len(lst)
        else:  # )로 닫혔지만 앞에가 ( 아니라면 이미 끝난거
            lst.pop()
            result += 1

print(result)
