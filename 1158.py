n, k = map(int, input().split())
arr = [i for i in range(1, n + 1)]
answer = []
num = k - 1

for i in range(n):
    if len(arr) > num:
        answer.append(arr.pop(num))
        num += k - 1
    elif len(arr) <= num:
        num = num % len(arr)
        answer.append(arr.pop(num))
        num += k - 1

print("<", ', '.join(str(i) for i in answer), ">", sep='')
