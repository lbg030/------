n,*l=open(0)
mylist = [*l]
print("n = ", n,"/ / *l = ", *l)
for elm in mylist:
    print(type(elm))