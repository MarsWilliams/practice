from collections import Counter
"""
Given a string containing only the characters x and y, find whether
there are the same number of xs and ys.

balanced("xxxyyy") => true
balanced("yyyxxx") => true
balanced("xxxyyyy") => false
balanced("yyxyxxyxxyyyyxxxyxyx") => true
balanced("xyxxxxyyyxyxxyxxyy") => false
balanced("") => true
balanced("x") => false
"""

def balanced(string: str) -> bool:

    c = Counter(string)

    if c['x'] == c['y']:
        return True

    return False


print(balanced("xxxyyy"))
print(balanced("yyyxxx"))
print(balanced("xxxyyyy"))
print(balanced("yyxyxxyxxyyyyxxxyxyx"))
print(balanced("xyxxxxyyyxyxxyxxyy"))
print(balanced(""))
print(balanced("x"))


"""
Optional bonus
Given a string containing only lowercase letters, find whether 
every letter that appears in the string appears the same number of 
times. Don't forget to handle the empty string ("") correctly!

balanced_bonus("xxxyyyzzz") => true
balanced_bonus("abccbaabccba") => true
balanced_bonus("xxxyyyzzzz") => false
balanced_bonus("abcdefghijklmnopqrstuvwxyz") => true
balanced_bonus("pqq") => false
balanced_bonus("fdedfdeffeddefeeeefddf") => false
balanced_bonus("www") => true
balanced_bonus("x") => true
balanced_bonus("") => true
Note that balanced_bonus behaves differently than balanced for a 
few inputs, e.g. "x".
"""

def balanced_bonus(string: str) -> bool:

    c = Counter(string)

    if not string or len(c) == 1 or len(set(c.values())) == 1:

        return True

    return False


print(balanced_bonus("xxxyyyzzz"))  # true
print(balanced_bonus("abccbaabccba"))  # true
print(balanced_bonus("xxxyyyzzzz"))  # false
print(balanced_bonus("abcdefghijklmnopqrstuvwxyz"))  # true
print(balanced_bonus("pqq"))  # false
print(balanced_bonus("fdedfdeffeddefeeeefddf"))  # false
print(balanced_bonus("www"))  # true
print(balanced_bonus("x"))  # true
print(balanced_bonus(""))  # true
