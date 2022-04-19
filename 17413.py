stack = input()
tempList = []
checked = 0
ans = []

print(stack)

for i in range(len(stack)):
    if(stack[i] == '<'):
        checked = 1

    if(checked == 0):
        tempList.append(stack[i])

    if(checked == 1):
        ans.append(stack[i])
