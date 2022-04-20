from sys import stdin

s = list(stdin.readline().rstrip())
# 정답 체크용
correct = input()

idx = 0

ans = ''
temp = ''
checked = 0
# print(s)
for i in range(len(s)):
    if(s[i] == '<'):
        idx = i
        checked = 1
        ans += temp[::-1]
        temp = ''

    if checked == 1:
        if(s[i] == '>'):
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

ans += temp[::-1]
print(ans)


# for i in range(len(ans)):
#     if(ans[i] != correct[i]):
#         print(f"i = {i} and ans[i] = {ans[i]}")

# print(correct == ans)
