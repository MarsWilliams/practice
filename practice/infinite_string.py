"""
You are given a string and a num of characters to consider.
You must count occurrences of 'a' in num character to consider.
#1 Iterate through string, counting 'a's.
#2 If you reach string end and num characters to consider is not
reached, start from the beginning.
This sounds like a while loop.
Or, sounds like it could be recursive.
This sounds like o(n)
"""

def repeatedStringRecursive(s, n, count=0):

    for char in s:
        if char == 'a':
            count += 1
        if n == 0:
            return count
        else:
            n -= 1
    if n > 0:
        return repeatedStringRecursive(s, n, count)
    return count


# print(repeatedStringRecursive('bac', 10))


def repeatedStringForLoop(s, n):
    s_len = len(s)
    if n % s_len == 0:
        repeated = s * (n // s_len)
    else:
        repeated = s * (n // s_len) + s
    count = 0
    for c in repeated:
        if c == 'a':
            count += 1
    return count

# print(repeatedStringForLoop('bac', 10))


def repeatedStringForDivMod(s, n):
    quotient, remainder = divmod(n, len(s))
    count = s.count('a') * quotient
    substr_count = s.count('a', 0, remainder)
    return count + substr_count

# print(repeatedStringForDivMod('bbbba', 49))


def repeatedStringOnePass(s, n):
    quotient, remainder = divmod(n, len(s))
    count = 0
    for i, c in enumerate(s):
        if c == 'a':
            if i < remainder:
                count += 1
            count += quotient
    return count


print(repeatedStringOnePass('abbbbbbbba', 99))
