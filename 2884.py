h, m = map(int, input().split())

if(m - 45 < 0):
    h = h-1
    m = 60 + m - 45
    if(h < 0):
        h = 24 + h
else:
    m = m - 45
print(h, m)
