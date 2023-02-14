a = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"
lst = a.split()
lst2 = [int(i) for i in lst]
print(f'{max(lst2)} {min(lst2)}')