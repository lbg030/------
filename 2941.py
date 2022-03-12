a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpha = input()
for t in a:
    alpha = alpha.replace(t, '*')
    # print(f"alpha change t='{t}' alpha = {alpha}")
# print(alpha)
print(len(alpha))
