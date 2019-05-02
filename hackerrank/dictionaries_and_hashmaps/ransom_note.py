from collections import Counter
from typing import List


def ransom_note(magazine: List[str], note: List[str]):
    """Given the words in the magazine and the words in the ransom
    note, print Yes if he can replicate his ransom note exactly using
    whole words from the magazine; otherwise, print No.
    For example, the note is "Attack at dawn". The magazine contains
    only "attack at dawn". The magazine has all the right words,
    but there's a case mismatch. The answer is NO.

    Function Description
    Complete the checkMagazine function in the editor below. It must
    print YES if the note can be formed using the magazine, or NO.
    """
    magazine_words = Counter(magazine)
    ransomable = True
    for word in note:
        if word not in magazine_words:
            ransomable = False
        if word in magazine_words:
            magazine_words[word] -= 1
            if magazine_words[word] < 0:
                ransomable = False
    return 'Yes' if ransomable else 'No'


print(ransom_note(
    'give me one grand today night'.split(),
    'give one grand today'.split()))


print(ransom_note('two times three is not four'.split(),
                  'two times two is four'.split()))
