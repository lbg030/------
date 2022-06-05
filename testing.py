a,b,c = map(int, input("세 수를 입력하시오 : ").split())

def mean3(a,b,c):
    result = round( ((a+b+c) / 3),1)
    print(f"{a}, {b}, {c}의 평균값은 {result}")
    max3(a,b,c)
    
def max3(a,b,c):
    result = max(min(a,b),c)
    print(f"{a}, {b}, {c}의 최댓값은 {result}")
    min3(a,b,c)

def min3(a,b,c):
    result = min(min(a,b),c)
    print(f"{a}, {b}, {c}의 최솟값은 {result}")
    
mean3(a,b,c)