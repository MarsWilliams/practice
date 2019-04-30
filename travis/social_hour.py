from collections import Counter


def social_hour(n: int) -> int:
    """
    Social Hour
    During social hour at the Grange Hall, every farmer shakes the
    hand of
    every other farmer once. Given n farmers, how many handshakes
    occur?
    2 -> 1
    3 -> 3
    Hints: Calculate 2-5 by hand. The function should be a one line
    formula.
    The generic term for this problem is n choose 2.
    """
    return n * (n-1) // 2


print(social_hour(3))


def social_hour_two(trades: str) -> dict:
    """
    Social Hour 2
    During social hour at the Grange Hall, there are a variety of
    tradesmen.
    Given a string where the letter represents the trade of that
    person,
    return a dictionary with the count of each trade.
    'acbabaaa' -> {'a': 5, 'b': 2, 'c': 1}
    """
    return dict(Counter(trades))


print(social_hour_two('acbabaaa'))


def social_hour_three(trades: str) -> int:
    """
    Social Hour 3
    During social hour at the Grange Hall, there are a variety of
    tradesmen.
    Every person shakes the hand of every other person with the same
    trade once. Given a string where the letter represents the
    trade of
    that person, calculate how many total handshakes occur.
    'acbabaaa' -> 11
    """
    trades_counts = Counter(trades)
    handshakes = 0
    for trade in trades_counts:
        handshakes += trades_counts[trade] * (trades_counts[
                                                  trade]-1) // 2
    return handshakes


print(social_hour_three('acbabaaa'))
