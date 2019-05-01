from collections import Counter

"""
Two strings are anagrams of each other if the letters of one string
can be rearranged to form the other string. Given a string,
find the number of pairs of substrings of the string that
are anagrams of each other.


Function Description
Complete the function sherlockAndAnagrams in the editor below.
It must return an integer that represents the
number of anagrammatic pairs of substrings in s.

sherlockAndAnagrams has the following parameter(s):
s: a string .


Input Format
The first line contains an integer q, the number of queries.
Each of the next q lines contains a string s to analyze.
String s contains only lowercase letters  ascii[a-z].


Output Format
For each query, return the number of unordered anagrammatic pairs.


Sample Input 0
2
abba
abcd

Sample Output 0
4
0
"""


def sherlockAndAnagrams(s: str) -> int:
    permutations = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            permutations.append(s[i:j + 1])

    counts = Counter([frozenset(Counter(substring).items()) for
                      substring in permutations])

    return sum(v * (v-1) // 2 for v in counts.values())


print(sherlockAndAnagrams('abba'))
