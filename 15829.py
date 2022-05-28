n = int(input())
string = input()

answer = 0
i = 0
for x in string:
    a = ord(x) - 96
    answer += a * (31**i)
    i += 1
print(answer % 1234567891)