# capital letters


def capitalize(i):
    first_small = i[0].upper()
    return first_small + i[1:]


words = str(input()).split()
res = []
for i in words:
    res.append(capitalize(i))
print(' '.join(res))
