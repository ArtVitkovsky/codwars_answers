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

