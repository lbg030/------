assignment = [True] + [False] * 30

for _ in range(28):
    k = int(input())
    assignment[k] = True
    
for idx, x in enumerate(assignment):
    if x == False:
        print(idx)