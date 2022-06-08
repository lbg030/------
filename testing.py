def f(x):
    n = len(x)
    for k in range(n-1) :
        if x[k] > x[k+1]:
            x[k], x[k+1] = x[k+1], x[k]
            
    return x


print(f([40,30,10,20]))