# Complete the function so that it finds the average of the three scores passed to it and returns the letter value
# associated with that grade.

def get_grade(s1, s2, s3):
    lst = [s1, s2, s3]
    ball = (sum(lst) / len(lst))
    if int(ball) in range(90, 100):
        return 'A'
    elif int(ball) in range(80, 90):
        return 'B'
    elif int(ball) in range(70, 80):
        return 'C'
    elif int(ball) in range(60, 70):
        return 'D'
    elif int(ball) in range(0, 60):
        return 'F'
