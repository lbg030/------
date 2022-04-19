stack = list(input().split())
checked = 0
print(stack)
for i in range(len(stack)):
    if(stack[i] == '<'):
        checked = 1

    elif(stack[i] == '>'):
        checked = 0

    if(checked == 1):
        print(stack[i])
