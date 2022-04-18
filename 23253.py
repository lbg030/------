n, m = map(int, input().split())
n_stack = []
stack = []
for _ in range(m):
    n_stack.append(int(input()))
    stack.append(list(map(int, input().split())))

print(n_stack, stack)
