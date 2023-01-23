def make_upper_case(s):
    return s.upper()


# Given a year, return the century it is in.
def century(year):
    import math as m
    cent = len(str(year))
    if year in range(0, 100):
        return 1
    elif cent >= 3 and year % 100 != 0:
        return m.floor((year / 100) + 1)
    elif cent >= 3 and year % 100 == 0:
        return int(year / 100)
