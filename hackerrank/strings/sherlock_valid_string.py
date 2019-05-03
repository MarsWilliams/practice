from collections import Counter

def isValid(s):
    """
    Function Description
    Complete the isValid function in the editor below.
    It should return either the string YES or the string NO.

    isValid has the following parameter(s):
    s: a string

    Input Format
    A single string s.

    Output Format
    Print YES if string s is valid, otherwise, print NO.

    Sample Input 0
    aabbcd

    Sample Output 0
    NO
    """
    counts = list(Counter(s).values())
    invalid = 0
    current = counts[0]
    for i in range(1, len(counts)):
        if counts[i] != current:
            invalid += 1
        if invalid > 1:
            return 'NO'
    return 'YES'



print(isValid('abcdefghhgfedecba'))
