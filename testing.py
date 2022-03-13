sen = "So when I die (the [first] I will see in (heaven) is a score list)."

leftsmall = 0
rightsmall = 0
leftbig = 0
rightbig = 0

for j in range(len(sen)):
    if('(' == sen[j]):
        leftsmall += 1
    if('[' == sen[j]):
        leftbig += 1
    if(')' == sen[j]):
        rightsmall += 1
    if(']' == sen[j]):
        rightbig += 1


print(
    f"번째 leftsmall = {leftsmall}, rightsmall = {rightsmall} leftbig = {leftbig} rightbig = {rightbig}")
