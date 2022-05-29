a = int(input("1보다 큰 양의 정수를 입력하세요. "))

answer = 1
for i in range(1,a+1):
    answer = answer * i

print("factorial data :", answer)