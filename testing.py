def not_binary(n):
    n = bin(n)
    k = ''
    for i in range(2, len(n)):
        if n[i] == '1' :
            k += '0'
        else :
            k += '1'
    print(k)
    return int(k,2)

print(not_binary(20))