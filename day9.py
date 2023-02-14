# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
# Return the resulting string.
# Note: input will never be an empty string

def fake_bin(x):
    lst = [i for i in x]
    lst2 = []
    for j in lst:
        if int(j) < 5 and j.isdigit():
            lst2.append(str(0))
        else:
            lst2.append(str(1))
    return ''.join(lst2)


# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence.
# You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful,
# there shouldn't be a space at the beginning or the end of the sentence!

def smash(words):
    a = ' '.join(words)
    return a.strip()

# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the
# number of sheep present in the array (true means present).


def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)


# In this little assignment you are given a string of space separated numbers, and have to return the highest and
# lowest number

def high_and_low(numbers):
    lst = numbers.split()
    lst2 = [int(i) for i in lst]
    return f'{max(lst2)} {min(lst2)}'

def better_than_average(class_points, your_points):
    average_point = (sum(class_points) + your_points) / (len(class_points) + 1)
    if average_point < your_points:
        return True
    else:
        return False

print(better_than_average([2, 3], 4))