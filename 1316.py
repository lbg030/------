n = int(input())

li = [True for _ in range(n)]
cnt = 0
for i in range(n):
    sen = input()
    res = True
    # 인덱스 차이가 2이상 나면 false else : true
    # len(n)만큼 list 생성 후 true, false값 넣고 true count ?
    for j in range(len(sen)-1):
        if(sen[j] != sen[j+1] and sen[j] in sen[j+1:]):
            li[i] = False
            break
    if(li[i]):
        cnt += 1

print(cnt)
# print(f"li = {li}")
