N = int(input())
dic = {}
numbers = [9,8,7,6,5,4,3,2,1,0]
sum = 0
for _ in range(N):
    string = input()
    i = 1
    for x in string:
        if x in dic:
            dic[x] += 10 ** (len(string) - i)
        else :
            dic[x] = 10 ** (len(string) - i)
        
        i += 1
        
lst = (sorted(dic.values(), reverse=True))

for x,y in zip(lst,numbers):
    sum += x * y
    
print(sum)