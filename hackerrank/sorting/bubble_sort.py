from typing import List

def bubble_sort(a: List[int]):
    """
    Given an array of integers, sort the array in ascending order using
    the Bubble Sort algorithm above. Once sorted, print the following
    three lines:

    Array is sorted in numSwaps swaps, where  numSwaps is the number of
    swaps that took place.
    First Element: firstElement, where firstElement is the first
    element in the sorted array.
    Last Element: lastElement, where lastElement is the last
    element in the sorted array.
    Hint: To complete this challenge, you must add a variable that keeps
    a running tally of all swaps that occur during execution.

    For example, given a worst-case but small array to sort: a = [6,4,1]
    we go through the following steps:
    swap    a
    0       [6,4,1]
    1       [4,6,1]
    2       [4,1,6]
    3       [1,4,6]
    It took 3 swaps to sort the array. Output would be:
    Array is sorted in 3 swaps.
    First Element: 1
    Last Element: 6

    for (int i = 0; i < n; i++) {

        for (int j = 0; j < n - 1; j++) {
            // Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]) {
                swap(a[j], a[j + 1]);
            }
        }

    }
    """
    num_swaps = 0

    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j + 1]:
                num_swaps += 1
                a[j], a[j+1] = a[j+1], a[j]

    first_element = a[0]
    last_element = a[-1]

    print('Array is sorted in {} swaps.'.format(num_swaps))
    print('First Element: {}'.format(first_element))
    print('Last Element: {}'.format(last_element))


print(bubble_sort([3, 2, 1]))
