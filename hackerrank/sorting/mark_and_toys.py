from typing import List

def marks_toys(prices: List[int], dollars_to_spend: int) -> int:
    """
    Function Description

    Complete the function maximumToys in the editor below.
    It should return an integer representing the maximum number
    of toys Mark can purchase.

    maximumToys has the following parameter(s):

    prices: an array of integers representing toy prices
    k: an integer, Mark's budget
    Input Format

    The first line contains two integers, n and k, the number of
    priced
    toys and the amount Mark has to spend.
    The next line contains  space-separated integers

    Output Format

    An integer that denotes the maximum number of toys Mark can
    buy for his son.

    Sample Input
    7 50
    1 12 5 111 200 1000 10

    Sample Output
    4
    """
    num_toys = 0
    price_total = 0
    for i in sorted(prices):
        if price_total + i <= dollars_to_spend:
            price_total += i
            num_toys += 1
        else:
            return num_toys

print(marks_toys([13, 12, 11, 111, 200, 1000, 10], 50))


print(marks_toys([1, 2, 3, 4], 7))
