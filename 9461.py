# DP 문제


n = int(input())
for _ in range(n):
    li = [1, 1, 1]
    m = int(input())
    if(m <= 3):
        print(li[m-1])
    else:
        for i in range(3, m):
            li.append(int(li[i-3] + li[i-2]))
        print(li[-1])
