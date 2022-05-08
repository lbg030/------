from sys import stdin

s = list(stdin.readline().rstrip())

# 정답 체크용
# correct = input()


idx = 0

ans = ''
temp = ''
checked = 0
# print(s)
for i in range(len(s)):
    if(s[i] == '<'):
        # 어디까지 괄호인지 확인하기 위해 idx 저장
        idx = i
        checked = 1
        # 지금까지 저장 된 값 뒤집어서 넣기
        ans += temp[::-1]
        # 값을 넣어줬으니 temp 초기화
        temp = ''

    if checked == 1:
        if(s[i] == '>'):
            # 괄호가 끝난 시점이므로 idx 부터 현재까지 ans에다가 저장 하고 괄호 해제 되었으니
            # checked = 0 으로 초기화
            ans += ''.join(s[idx:i+1])
            checked = 0
        else:
            continue

    # checked = 0일때
    else:
        if(s[i] == ' '):
            ans += temp[::-1] + ' '
            temp = ''
        else:
            temp += s[i]

# 괄호를 만나지 못해 아직 저장 하지 못한 temp값 추가
ans += temp[::-1]
print(ans)


# for i in range(len(ans)):
#     if(ans[i] != correct[i]):
#         print(f"i = {i} and ans[i] = {ans[i]}")

# print(correct == ans)
