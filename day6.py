# You get an array of numbers, return the sum of all of the positives ones.

def positive_sum(arr):
    score = 0
    for i in arr:
        if i >= 0:
            score += i
    return score


print(positive_sum([1, -4, 7, 12]))
