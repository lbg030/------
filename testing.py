a = input()
b = ''
for i in range(len(a)):
    if not b :
        b += a[i]
        continue
    
    else :
        if b[-1] == ' ' and a[i] == ' ':
            continue

    b += a[i]
print(b)