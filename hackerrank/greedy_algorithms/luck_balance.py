"""
Complete the luckBalance function in the editor below. It should
return an integer that represents the maximum luck balance achievable.

luckBalance has the following parameter(s):

k: the number of important contests Lena can lose
contests: a 2D array of integers where each contests[i] contains two
integers
that represent the luck balance and importance of the ith contest.
By hand procedure:
sort important contests by luck
take k from that list with max luck (to loose) + all non important
contest luck sums.
subtract luck sum from total remaining important contests
"""


def luck_balance(k, contests):
    p = sorted(contests, key=lambda x: (-x[1], -x[0]))
    top_k_loses = sum(x[0] for x in p[:k])
    loses = sum(x[0] for x in p[k:] if x[1] == 0)
    top_wins = sum(x[0] for x in p[k:] if x[1] == 1)
    return (top_k_loses + loses) - top_wins


print(luck_balance(3, [(5, 1),
                       (2, 1),
                       (1, 1),
                       (8, 1),
                       (10, 0),
                       (5, 0)]))


def faster_luck_balance(k, contests):
    sorted_contests = sorted(contests, key=lambda x: (-x[1], -x[0]))
    balance = sum(x[0] for x in sorted_contests[:k])
    for i in sorted_contests[k:]:
        luck, importance = i
        if importance == 1:
            balance -= luck
        else:
            balance += luck
    return balance


print(faster_luck_balance(3, [(5, 1),
                              (2, 1),
                              (1, 1),
                              (8, 1),
                              (10, 0),
                              (5, 0)]))
