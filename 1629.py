n,m,d = map(int, input().split())
k = 1
n = n % d
lst = [n]
answer = 0
while True:
    x = (lst[-1] * n) % d
    # print(x)
    if x not in lst:
        lst.append(x)
        k += 1
    elif x == lst[-1]:
        answer = x
        break
    else :
        answer = lst[(m % len(lst)) - 1]
        break

print(answer)
# print(lst)