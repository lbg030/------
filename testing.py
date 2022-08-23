S, P = map(int, input().split())
dna = list(input())
tmp = list(map(int, input().split()))
dic = {'A': tmp[0], 'C': tmp[1], 'G': tmp[2], 'T': tmp[3]}
base = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

count = 0
for i in range(S-P+1):
    flag = True

    if i == 0:
        for j in range(P):
            base[dna[j]] += 1
    else:
        base[dna[i+P-1]] += 1
        base[dna[i-1]] -= 1

    for i in ('A', 'C', 'G', 'T'):
        if base[i] < dic[i]:
            flag = False
            break

    if flag:
        count += 1

print(count)
