from collections import Counter
from typing import List


def anagram_finder(str1: str, str2: str) -> bool:
    """
    Anagram Finder
    Given two strings, return if the strings are anagrams.
    'hall', 'hlal' -> True
    Hint: Use Counter
    """
    return Counter(str1) == Counter(str2)


print(anagram_finder('hall', 'hlal'))


def anagram_finder_two(strings: List[str]) -> int:
    """
    Anagram Finder 2
    An "anagram family" is a group of words that can be anagrams of
    each other. Given a list of strings, return how many anagram
    families there are.
    ['hall', 'hlal', 'grange'] -> 2
    Hint: You can make a dictionary hashable by calling frozenset
    on .items()
    """
    return len(set([frozenset(Counter(string).items())
                    for string in strings]))


print(anagram_finder_two(['hall', 'hlal', 'grange']))


def anagram_finder_three(strings: List[str]) -> int:
    """
    Anagram Finder 3
    An "anagram pair" is two strings that can be anagrams of each other.
    Given a list of strings, return an integer of how many
    anagram pairs there are.
    ['hall', 'hlal', 'hlla', 'grange', 'ggrane'] -> 4
    They are: (('hall', 'hlal'), ('hall', 'hlla'), ('hlal', 'hlla),
    ('grange', 'ggrane'))
    """

    letter_counts = Counter([frozenset(Counter(string).items()) for
                             string in strings])
    pairs = 0

    for counts in letter_counts:
        pairs += letter_counts[counts] * \
                 (letter_counts[counts]-1) // 2

    return pairs


print(anagram_finder_three(['hall', 'hlal', 'hlla',
                            'grange', 'ggrane']))
