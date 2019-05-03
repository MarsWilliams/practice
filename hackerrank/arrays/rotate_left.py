from typing import List


def rotate_left(a: List[int], d: int) -> List[int]:
    """
    Print a single line of  space-separated integers denoting
    the final state of the array after performing  left rotations.
    """
    return a[d:] + a[:d]


print(rotate_left([1, 2, 3, 4, 5], 4))
