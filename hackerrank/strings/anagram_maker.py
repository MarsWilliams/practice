from collections import Counter

def anagram_maker(a: str, b: str) -> int:
    """
    Complete the makeAnagram function in the editor below.
    It must return an integer representing the minimum
    total characters that must be deleted to make the strings
    anagrams.
    makeAnagram has the following parameter(s):
    a: a string
    b: a string"""
    ac = Counter(a)
    bc = Counter(b)
    return sum(list((ac - bc).values()) + list((bc - ac).values()))


print(anagram_maker('cde', 'abc'))

