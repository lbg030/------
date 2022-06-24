n = int(input())

binary = str(bin(n)[2:])
# print(binary.count(1))
cnt = 0
for x in binary:
    
    if x == '1':
        cnt += 1

print(cnt)