a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))
# print(result)
for i in range(10):
    print(result.count(str(i)))
