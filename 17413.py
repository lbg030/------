stack = list(input().split())
tempList = []
checked = 0
ans = []

print(stack)
# # print(stack)
# for k in range(len(stack)):
#     for i in range(len(stack[k])):
#         if(stack[k][i] == '<'):
#             checked = 1
#             ans.extend(tempList[::-1])

#         elif(stack[k][i] == '>'):
#             checked = 0
#             tempList = []

#         if(checked == 1):
#             ans.append(stack[k][i])
#             # print(stack[k][i])

#         elif(checked == 0):
#             tempList.append(stack[k][i])
#     print(f"ans = {ans}")
#     print(f"tempList = {tempList}")
# print(''.join(ans))
