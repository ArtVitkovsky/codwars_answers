a = '12345679'
b = [i for i in a]
c = len(b)
for j in b:
    if int(j) < 5:
        b[b.index(str(j))] = str(0)
    else:
        b[b.index(str(j))] = str(1)
print(''.join(b))
