#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_scores = 0
    total_weight = 0
    for scores, weight in my_list:
        total_scores += scores * weight
        total_weight += weight
        weight_av = total_scores / total_weight if total_weight != 0 else 0
    return weight_av
