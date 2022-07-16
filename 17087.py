n,m = map(int, input().split())

temp = map(int, input().split())
lst = list(set(map(lambda x:abs(x-m), temp)))

# print(lst)
def GCDofTwoNumbers(a, b):
    while b != 0:
        a, b = b, a%b
    return a

gcd = min(lst)

for i in range(len(lst)):
    gcd = GCDofTwoNumbers(lst[i], gcd)

print(gcd)

def gcd(a, b):
    while b:
        mod = b
        b = a%b
        a = mod
    return a

n, s = map(int, input().split())
a = list(map(int, input().split()))
dif = list(set(abs(a[i]-s) for i in range(n)))
d = min(dif)
for i in range(len(dif)):
    d = gcd(dif[i], d)
    
print(d)