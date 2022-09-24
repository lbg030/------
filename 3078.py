n, m = map(int, input().split())

lst = [len(input()) for _ in range(n)]
dic = {}
cnt = 0
end = m

for i in range(m):
    if lst[i] in dic :
        dic[lst[i]] += 1 
    else :
        dic[lst[i]] = 1

# print(dic)
    
for i in range(len(lst)):
    dic[lst[i]] -= 1
    if i+ m < len(lst):
        if lst[i+m] in dic:
            dic[lst[i+m]] += 1
        else :
            dic[lst[i+m]] = 1
     
    cnt += dic[lst[i]]
    # print(dic,lst[i])
print(cnt)