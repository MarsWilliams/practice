from typing import List

"""
Falling Sign
The sign over the Grange Hall is falling apart. Each letter is
disappearing one by one, from the left side.
Given a string, return a list of strings of how the sign will look over time.
'hall' -> ['hall', 'all', 'll', 'l']
Hints: Use a for loop and slicing
"""


def falling_sign(sign: str) -> List[str]:
    return [sign[i:] for i in range(len(sign))]


print(falling_sign('hall'))


"""
Falling Sign 2
They're rebuilding the sign over the Grange Hall. One letter is being 
added at a time to the right side. Given a string, 
return a list of strings of how the sign will look over time.
'hall' -> ['h', 'ha', 'hal', 'hall']
Hints: Use a for loop and slicing
"""


def falling_sign_two(sign):
    return [sign[:i] for i in range(1, len(sign) + 1)]


print(falling_sign_two('hall'))


"""
Falling Sign 3
The sign over the Grange Hall is falling apart. Each letter is 
disappearing one by one, but from either the left or the right. 
Given a string, return a list of all possible states of the sign.
'hall' -> ['h', 'ha', 'hal', 'hall', 'a', 'al', 'all', 'll', 'l']
Hint: Use nested for loops and slicing
"""


def falling_sign_three(sign):
    permutations = set()
    for i in range(len(sign) + 1):
        for j in range(len(sign)):
            if sign[j:i]:
                permutations.add(sign[j:i])
    return list(permutations)


print(falling_sign_three('hall'))
