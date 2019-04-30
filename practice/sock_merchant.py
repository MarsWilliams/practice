"""
Given n (len of array) and array of ints, determine how many
pairs of ints there are.
Seems like you could use counter.
Then you would need to make another pass, dividing each counter
value by 2.
Seems like 1 pass should be enough.
Seems like you don't need n.
sample = [10, 20, 20, 10, 10, 30, 50, 10, 20]
"""

from collections import Counter


def sockMerchantCounter(n, ar):
    counts = Counter(ar)
    return sum((counts[color]//2 for color in counts))


print(sockMerchantCounter(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))


def sockMerchantCounterGolf(n, ar):
    return sum((count//2 for count in Counter(ar).values()))


print(sockMerchantCounterGolf(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))


def sockMerchantOnce(n, ar):
    counts = {}
    pairs = 0
    for color in ar:
        counts[color] = counts.get(color, 0) + 1
        if counts[color] == 2:
            pairs += 1
            counts[color] = 0
    return pairs


print(sockMerchantOnce(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))


def sockMerchantSpaceNew(n, ar):
    total = set()
    pairs = 0
    for i in ar:
        if i in total:
            pairs += 1
            total.remove(i)
        else:
            total.add(i)
    return pairs

print(sockMerchantSpaceNew(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))