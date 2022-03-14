n = int(input())


for i in range(n):
    k = input()
    cnt = 0  # )
    cnt2 = 0  # ()
    res = 0
    for j in range(len(k)):
        if(k[j] == ')'):
            cnt += 1
            # print(k[j])
        elif(k[j] == '('):
            cnt2 += 1
        if(cnt > cnt2):
            res = 1
    # print(f"cnt = {cnt}, cnt2 ={cnt2}")
    if(cnt == cnt2 and res == 0):
        print("YES")
    else:
        # print(f"{res}")
        print("NO")
