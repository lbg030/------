# silver 4
n = int(input())

count = 0

for i in range(1, n+1):
    a = i // 100
    b = (i % 100) // 10
    c = (i % 10)

    if(i < 10):
        count += 1
        # print(f"10까지 Count = {count}")
    elif(i < 100):
        count += 1
        # print(f"100까지 I = {i}, Count={count}")
    else:
        if(((b-a == c-b) or (a-b == b-c))):
            count += 1

print(count)
# i = 11

# a = i // 100
# b = (i % 100) // 10
# c = (i % 10)

# print(a, b, c)
