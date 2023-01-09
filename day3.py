# Given a non-empty array of integers, return the result of multiplying the values together in order
def grow():
    arr = [4, 1, 3, 2]
    brr = sorted(arr)
    res = 1
    for i in brr:
        res *= i
    return res

