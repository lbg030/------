from math import factorial

num = factorial(int(input()))
count = 0
i = 1

# print(num)
# print(str(num)[-3])
while True:
    # print(str(num)[-i])
    if(str(num)[-i] == '0'):
        count += 1
        i += 1
    else:
        break

print(count)
