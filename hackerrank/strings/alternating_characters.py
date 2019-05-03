
def alternatingCharacters(s: str) -> int:
    """
    Function Description

    Complete the alternatingCharacters function in the editor below.
    It must return an integer representing the minimum
    number of deletions to make the alternating string.

    alternatingCharacters has the following parameter(s):

    s: a string
    Input Format

    The first line contains an integer q, the number of queries.
    The next q lines each contain a string s.

    Output Format
    For each query, print the minimum number of deletions required
    on a new line.

    Sample Input
    5
    AAAA
    BBBBB
    ABABABAB
    BABABA
    AAABBB

    Sample Output
    3
    4
    0
    0
    4
    Explanation
    The characters marked red are the ones that can be deleted so that
    the string doesn't have matching consecutive characters.
    """
    num_deletions = 0
    current = s[0]
    for i in range(1, len(s)):
        print(s[i])
        if s[i] == current:
            num_deletions += 1
        else:
            current = s[i]
    return num_deletions


print(alternatingCharacters('AAAA'))
print(alternatingCharacters('AAABBB'))

