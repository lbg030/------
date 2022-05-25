
Case = int(input())
target = list(map(str, input().split('*')))
first = len(target[0])
last = len(target[1])
#별표는 문자열의 시작과 끝에 있지 않음 -> 무조건 2개로 나눠짐.
for i in range(Case):    
    compared = input()
    
    if target[0] == compared[:first]:
        compared = compared[first:]
        if len(compared) == 0 :
            print("NE")
            continue
        # print(compared)
        if target[1] == compared[-last:]:
            print("DA")
        else :
            print("NE")
    else :
        print("NE")
    