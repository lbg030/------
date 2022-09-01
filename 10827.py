from decimal import Decimal, getcontext
 
a, b = map(str,input().split())
 
getcontext().prec = 10000
print("{0:f}".format(Decimal(a)**int(b)))