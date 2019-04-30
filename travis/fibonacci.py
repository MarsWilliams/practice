from typing import List
"""Sequnce that starts with the numbers 0, 1. You get the next number in the sequence by adding the two previous numbers
For example: [0, 1, 1, 2, 3, 5, 8, 13]
Given a positive integer n, calculate n digits of the fibonacci sequence.
Do so iteratively and recursively.
"""


def fib_iter(n: int) -> List[int]:

    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[:n]


print(fib_iter(3))
print(fib_iter(5))


def fib_rec(n: int, fib_sequence: List[int] = None) -> List[int]:

    if fib_sequence is None:
        fib_sequence = [0, 1]

    if len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

        return fib_rec(n, fib_sequence)

    return fib_sequence[:n]


print(fib_rec(3))
print(fib_rec(5))


def fib_n_iter(n: int) -> int:

    count = 0
    current = 0
    proxima = 1

    while count < n:
        current, proxima = proxima, current + proxima
        count += 1

    return current


print(fib_n_iter(3))
print(fib_n_iter(5))


def fib_n_recursive(n: int, current: int = 0, proxima: int = 1) -> int:

    if n != 0:

        return fib_n_recursive(n-1, proxima, current + proxima)

    return current


print(fib_n_recursive(3))
print(fib_n_recursive(5))


def fib_ceiling_n_iter(n: int) -> int:
    current = 0
    proxima = 1

    while proxima <= n:
        current, proxima = proxima, current + proxima

    return current


print(fib_ceiling_n_iter(3))
print(fib_ceiling_n_iter(5))


def fib_ceiling_n_recursive(n: int, current: int = 0, proxima: int = 1) -> int:

    if proxima <= n:
        return fib_ceiling_n_recursive(n, proxima, current + proxima)

    return current


print(fib_ceiling_n_recursive(3))
print(fib_ceiling_n_recursive(5))


def fib_natural_member_iter(n: int) -> bool:
    """given a natural number >= 0, return true if its in the sequence, false if it is not"""

    current = 0
    proxima = 1

    while current < n:

        current, proxima = proxima, current + proxima

    return n == current


print(fib_natural_member_iter(3))
print(fib_natural_member_iter(1))
print(fib_natural_member_iter(11))


def fib_natural_member_recursive(n: int, current: int = 0, proxima: int = 1) -> bool:
    """given a natural number >= 0, return true if its in the sequence, false if it is not"""

    if current < n:

        current, proxima = proxima, current + proxima

        return fib_natural_member_recursive(n, current, proxima)

    return n == current


print(fib_natural_member_recursive(3))
print(fib_natural_member_recursive(1))
print(fib_natural_member_recursive(11))


def fib_members(n: int) -> List[int]:
    """Given a whole number n, return a list of n+1 booleans where each item in the list represents if its 0-index is a Fibonacci number.
    6 -> [True, True, True, True, False, True, False]"""

    fibs = set()

    current = 0
    proxima = 1

    while current <= n:
        fibs.add(current)
        current, proxima = proxima, current + proxima

    return [x in fibs for x in range(n+1)]


print(fib_members(0))
print(fib_members(1))
print(fib_members(2))
print(fib_members(7))
print(fib_members(8))


def fib_members_recursive(n: int, current: int = 0, proxima: int = 1, fibs: set = None) -> List[int]:

    if fibs is None:
        fibs = set()

    if current <= n:
        fibs.add(current)
        return fib_members_recursive(n, proxima, current + proxima, fibs)

    return [x in fibs for x in range(n + 1)]


print(fib_members_recursive(3))
print(fib_members_recursive(1))
print(fib_members_recursive(11))
