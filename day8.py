# Complete the solution so that it returns true if the first argument(string) passed in ends with
# the 2nd argument
def solution(text, ending):
    if text[len(text) - len(ending)] == ending:
        return True
    else:
        return False


# Given a random non-negative number, you have to return the digits of this number within an array
# in reverse order.
def digitize(n):
    lst = [int(i) for i in str(n)]
    return lst[::-1]

#  convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith,
#  but they are not capitalized in the same way he originally typed them.


def to_jaden_case(string):
    lst_1 = string.split()
    lst_2 = [i.capitalize() for i in lst_1]
    return ' '.join(lst_2)

# Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple
# elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty
# array/list. Don't change the order of the elements that are left.


def remove_smallest(numbers):
    numbers.remove(min(numbers))
    return numbers

# Write a function which calculates the average of the numbers in a given list.
# Note: Empty arrays should return 0.


def find_average(numbers):
    if len(numbers) >= 1:
        return sum(numbers) / len(numbers)
    else:
        return 0

# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
# Return the resulting string.
# Note: input will never be an empty string
