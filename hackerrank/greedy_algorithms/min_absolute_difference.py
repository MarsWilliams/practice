from typing import List
from itertools import combinations
import math

def minimumAbsoluteDifference(arr: List[int]):
    """
    Function Description

    Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that represents the minimum absolute difference between any pair of elements.

    minimumAbsoluteDifference has the following parameter(s):

    n: an integer that represents the length of arr
    arr: an array of integers

    Input Format
    The first line contains a single integer n, the size of arr.
    The second line contains n space-separated integers arr[i].

    Output Format
    Print the minimum absolute difference between any two elements in the array.

    Sample Input 0
    3
    3 -7 0

    Sample Output 0
    3
    """
    s_arr = sorted(arr)
    return min(s_arr[i] - s_arr[i-1] for i in range(1, len(s_arr)))


print(minimumAbsoluteDifference([3, -7, 0]))

print(minimumAbsoluteDifference([-59, -36, -13, 1, -53, -92, -2, -96,
                                 -54, 75]))
