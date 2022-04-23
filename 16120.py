# p -> ppap로 바뀐것이기 때문에 결국 ppap -> p로 다시 바꾸어 준다면
# 이 문자열이 ppap로 구성되어 있는지 아닌지 확인 가능하다.

# pppapap -> pPap [ P = ppap ]
# ppapapp -> Papp [ P = ppap ] 이런식으로

w = input()
stack = []
ppap = ["P", "P", "A", "P"]
for i in range(len(w)):
    stack.append(w[i])
    # print(stack)
    if stack[-4:] == ppap:
        for _ in range(4):
            stack.pop()
        stack.append("P")

if stack == ppap or stack == ["P"]:
    print("PPAP")
else:
    print("NP")
