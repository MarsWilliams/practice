from collections import Counter
"""Given a string, return a new string keeping only the first occurrence of each character in order.
'caardc' -> 'card'"""

def string_eater(with_duplicates: str) -> str:

    uniques = set()

    without_duplicates = []

    for letter in with_duplicates:
        if letter not in uniques:
            without_duplicates.append(letter)
            uniques.add(letter)
    return ''.join(without_duplicates)


print(string_eater('faatboy'))
print(string_eater('faatbooy'))
print(string_eater('chubber'))



"""Given a string, return a new string keeping only the first two occurrences of each character in order.
'abacbabbcd' -> 'abacbcd'"""

def first_two(string: str) -> str:

    letters = list(string)

    counts = dict.fromkeys(letters, 0)

    first_two = []

    for letter in letters:
        if counts[letter] < 2:
            first_two.append(letter)
            counts[letter] += 1

    return ''.join(first_two)

print(first_two('faatboyyy'))
print(first_two('faaatbbooy'))
print(first_two('chubber'))


def first_two_counter(string: str) -> str:

    counts = Counter()

    first_two = []

    for letter in list(string):
        if counts.get(letter) < 2:
            first_two.append(letter)
            counts.update(letter)

    return ''.join(first_two)


print(first_two('faatboyyy'))
print(first_two('faaatbbooy'))
print(first_two('chubber'))

"""Given a string, return a new string keeping only the last occurrence of each character in order.
'caardc' -> 'card'"""

def last_occurence(string: str) -> str:

    counts = Counter(string)

    last_occurence = []

    for letter in string:
        counts[letter] -= 1
        if counts[letter] == 0:
            last_occurence.append(letter)

    return ''.join(last_occurence)


print(last_occurence('faatboyyy'))
print(last_occurence('faaatbbooy'))
print(last_occurence('chubber'))


def last_occurence_ala_travis(string: str) -> str:

    uniques = set()

    last_occurences = []

    for letter in reversed(string):
        if letter not in uniques:
            last_occurences.append(letter)
            uniques.add(letter)

    return ''.join(reversed(last_occurences))


print(last_occurence_ala_travis('faatboyyyfa'))
print(last_occurence_ala_travis('faaatbbooy'))
print(last_occurence_ala_travis('chubber'))

