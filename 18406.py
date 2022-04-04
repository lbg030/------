n = input()
m = n[:len(n)//2]
n = n[len(n)//2:]


m_total = 0
n_total = 0

for i in range(len(m)):
    m_total += int(m[i])
    n_total += int(n[i])

if(m_total == n_total):
    print('LUCKY')
else:
    print('READY')
