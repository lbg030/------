import math

d_1 = [0.9,0.05,0.05]
d_2 = [0.3,0.2,0.5]

lst = [d_1, d_2]
entropy = 0
for d in lst:
    for num in d:
        entropy += (num * math.log(num))
        # print(f"entropy += {num} * log{num}")
    # print(num)
    entropy *= -1
    print(d,"=",entropy)
    