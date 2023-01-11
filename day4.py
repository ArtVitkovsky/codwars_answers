# Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format
# "x:y", where x is our team's score and y is our opponents score.
def points(games):
    score = 0
    point = [i.split(':') for i in games]
    for j in point:
        if int(j[0]) > int(j[1]):
            score += 3
        elif int(j[0]) == int(j[1]):
            score += 1
    return score
