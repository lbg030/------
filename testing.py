#  K = K-(K&((~K)+1))
a = int(input())
binary_k = '0b' + input()
cnt = 0
decimal_k = int(binary_k[2:], 2)

def not_binary(n):
    k = ''
    for i in range(2, len(n)):
        if n[i] == '1' :
            k += '0'
        else :
            k += '1'
    return int(k,2)

def decimal_to_binary(n):
    return bin(n)

while True:
    binary_k = bin(decimal_k)
    middle = (decimal_k & ((not_binary(binary_k) + 1)))
    res = decimal_k - middle
    
    if res == 0 :
        cnt += 1
        print(cnt)
        break
    
    else :
        cnt += 1
        decimal_k = res
        # print(res)
        