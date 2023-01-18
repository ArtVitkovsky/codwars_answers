# Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by
# index! ).
def sum_array(arr):
    lst = []
    for i in arr:
        lst.append(i)
    lst.remove(min(lst))
    lst.remove(max(lst))
    return sum(lst)


print(sum_array({1, 1, 2, 3, 4}))

