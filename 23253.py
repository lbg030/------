# 간단하게 생각하면
# 결국 stacks 가 들어오는데 한개라도 내림차순으로 정렬이 안되어 있다면 결국 실패함.

n, m = map(int, input().split())
checked = 0
for _ in range(m):
    n_stack = int(input())
    stack = list(map(int, input().split()))
    if stack != sorted(stack, reverse=True):
        checked = 1
        break

print("Yes" if checked == 0 else "No")
# for i in range(n):
#     checked = 0
#     for j in range(m):
#         if(len(stack[j]) != 0):
#             if(stack[j][-1] == i+1):
#                 checked = 1
#                 stack[j].pop()
#                 break
#         else:
#             del stack[j]
#         print(stack)
#     if(checked == 0):
#         print("No")
#         break

# if(checked == 1):
#     print("Yes")
