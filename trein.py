def remove_smallest(numbers):
    new_tup = []
    if numbers is list:
        numbers.remove(min(numbers))
        return numbers


print(remove_smallest([2, 1, 8, 1, 9, 5]))