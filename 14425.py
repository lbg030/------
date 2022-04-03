n, m = map(int, input().split())
result_list = []
compared_list = []
count = 0
for _ in range(n):
    result_list.append(input())

for _ in range(m):
    compared_list.append(input())

# print(result_list, compared_list)

for x in compared_list:
    if x in result_list:
        count += 1

print(count)
