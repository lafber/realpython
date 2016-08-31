''' Real Python
    7.8 assignment simulate an election
    Simulate an election between two candidates, A and B. One of the candidates wins the overall election by a majority based on the outcomes of three regional elections. (In other words, a candidate wins the overall election by winning at least two regional elections.) Candidate A has the following odds:87% chance of winning region 1 65% chance of winning region 2 17% chance of winning region 3
'''

from random import random

candidate_a_wins = 0
candidate_b_wins = 0

def election_region(odd):
    if random() <= odd:
        return True
    return False

def election( ):

    region_win_candidate_a = 0
    region_win_candidate_b = 0
    
    # election region 1
    if election_region(0.87) == True:
        region_win_candidate_a += 1
    else:
        region_win_candidate_b += 1

    # election region 2
    if election_region(0.65) == True:
        region_win_candidate_a += 1
    else:
        region_win_candidate_b += 1

    # election region 3
    if election_region(0.17) == True:
        region_win_candidate_a += 1
    else:
        region_win_candidate_b += 1

    return region_win_candidate_a > region_win_candidate_b

'''
    if region_win_candidate_a > region_win_candidate_b:
        print("Candidate A win ", region_win_candidate_a, "regions")
    else:
        print("Candidate B win ", region_win_candidate_b, "regions")
'''

### MAIN

# Lets do 10 000 elections
for elections in range(1, 10001):
    if election() == True:
        candidate_a_wins += 1
    else:
        candidate_b_wins += 1

print("Probability that candidate A win is {} and candidate B is {}".format(candidate_a_wins/10000, candidate_b_wins/10000))
