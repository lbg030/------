alphabet = input()
# n = "c=c-"
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0

# print(n[0:2] in croatia)
a = alphabet[0:1]
for i in range(len(alphabet)):
    if(croatia[i] in alphabet):
        count += 1

# if(alphabet in croatia):
#     count += 1
# else:
# count += 1

# print(count)
