num = 58912365
lst = []
for i in str(num):
    lst.append(int(i))
sr = sorted(lst, reverse=True)
print(sr)
