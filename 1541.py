n = input().split('-')
li = []
sum = 0

# 0번째는 무조건 더해주기
for x in n[0].split('+'):
    sum += int(x)

# 나머지는 다 빼기
# int로 받으면 00002같은걸 인식 못하지만 int('0002')= 2로 나옴

for x in n[1:]:
    for j in x.split('+'):
        sum -= int(j)

print(sum)
