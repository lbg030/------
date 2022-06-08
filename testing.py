x, y = map(float, input("두 수를 입력하세요: ").split())

print("1.더하기 2. 빼기 3. 곱하기 4. 나누기")
method = int(input("계산 방식을 숫자로 선택하세요. "))


if method == 1:
    print(x+y)

elif method == 2:
    print(x - y)
    
elif method == 3:
    print(x*y)
    
else :
    if y == 0:
        print('0으로 나눌 수 없습니다.')
    else :
        print(x/y)