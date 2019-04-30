from typing import List


def collatz(n: int, ns: List[int] = None) -> List[int]:
    """
    Collatz conjecture is an unsolved mathematical problem. You can
    take any positive integer, and following step by step rules,
    you can always end up back at 1.
    Given a positive integer n, if it is even, divide it by 2. If
    it is odd, multiple it by 3 and add 1.
    Given a positive integer as an input, return a list, with 1 as
    the end of the sequence.
    """
    if n < 1:
        raise ValueError
    if ns is None:
        ns = []
    ns.append(n)
    if n == 1:
        return ns
    else:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
        return collatz(n, ns)


def collatz_iter(n: int) -> List[int]:
    """
    Collatz conjecture is an unsolved mathematical problem. You can
    take any positive integer, and following step by step rules,
    you can always end up back at 1.
    Given a positive integer n, if it is even, divide it by 2. If
    it is odd, multiple it by 3 and add 1.
    Given a positive integer as an input, return a list, with 1 as
    the end of the sequence.
    """
    if n < 1:
        raise ValueError

    ns = [n]

    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
        ns.append(n)

    return ns
