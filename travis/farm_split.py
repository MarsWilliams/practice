"""
Even split
Twin brothers inherit a farm made up of 1 meter squares.
The farm is a rectangle of shape n by n + 1.
They want to split the farm diagonally down the long side so they both
get the same amount of land.
x o o o o
x x o o o
x x x o o
x x x x o
Given n, calculate how many squares of land each brother gets.
Hints: Calculate 1-4 by hand. The function should be a
one line formula. The generic term for this problem is a triangle
number."""


def even_split(n):
    """
    (n-i, n-i, n-i, n-i...with i starting at 0 and approaching n)
    Could more simply be n*(n+1)/2
    """
    return sum((n-i for i in range(n)))


print(even_split(4))


"""
Smaller split
An older brother and a younger brother inherit a farm made up of 
1 meter squares.
The farm is a square of shape n x n. 
They want to split the farm diagonally with the older brother 
getting the bigger triangle and the younger brother getting 
the smaller triangle.
o o o o o
x o o o o
x x o o o
x x x o o
x x x x o
Given n, calculate how many squares of land the younger brother gets.
Hints: Calculate 2-5 by hand. The function should be a one 
line formula."""


def smaller_split(n):
    return sum((n-i for i in range(1, n)))


print(smaller_split(5))


"""
o o 
x o 
"""
print(smaller_split(2))

"""
o o o
x o o
x x o
"""
print(smaller_split(3))
