n , m =map(int, input().split())
string = input()
Minimum_DNA_Count_list = list(map(int, input().split()))
DNA_dic = {'A' : Minimum_DNA_Count_list[0],
           'C' : Minimum_DNA_Count_list[1],
           'G' : Minimum_DNA_Count_list[2],
           'T' : Minimum_DNA_Count_list[3]}

check_list = ['A','C','G','T']
cnt = 0

for i in range(n-m+1):
    flag = True
    
    if i == 0:
        for j in range(m):
            DNA_dic[string[j]] -= 1
    
    else :
        DNA_dic[string[i-1]] += 1
        DNA_dic[string[i+m-1]] -= 1
        
    for key in DNA_dic.keys():
        if DNA_dic[key] > 0:
            flag = False
            break
        
    if flag:
        cnt += 1
        
print(cnt)