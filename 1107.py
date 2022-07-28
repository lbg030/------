#반례 1000
# 9
# 0 1 2 3 4 5 6 7 8

n = input()
y = int(input())
if y == 0 :
    print(len(n))
elif n == '100':
    print("0")
else :
    lst = [i for i in range(10)]
    broken = list(map(int, input().split()))
    remoteControl = ''
    excepting = int(n)
    for x in broken :
        lst.remove(x)
    
    for i in range(len(n)):
        minDifference = 9
        num = 0
        for x in lst:
            if i == 0 and n[0] == '1':
                excepting = abs(int(n) - int((len(n)-1) * str(lst[-1]))) + len(n)-1
            
            if i == 0 and n[0] == '9':
                if lst[0] != 0 :
                    excepting = abs(int(n) - int((len(n)+1) * str(lst[0]))) + len(n) + 1
                else :
                    k = str(lst[1]) + (str(lst[0]) * len(n))
                    excepting = abs(int(n) - int(k)) + len(k)
                
            if i > 0 and n[i] == '0' and remoteControl[0] < n[0]:
                num = lst[-1]
            else : 
                if minDifference > abs(x - int(n[i])):
                    minDifference = abs(x - int(n[i]))
                    num = x
        remoteControl += str(num)
    
    # print(remoteControl)
    # print(excepting)
    print(min(len(str(remoteControl)) + abs(int(remoteControl)-int(n)), excepting))