#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    score = 0
    weights = 0

    for tup in my_list:
        score += tup[0] * tup[1]
        weights += tup[1]

    return (score / weights)
