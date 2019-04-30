"""
Given a 6 x 6 2d array, find all hourglass sums. An hourglass sum
is a sum of all values in the hourglass, defined as:
row[column] + row[column+1] + row[column+2]) +
row+1[column+1] +
row+2[column] + row+2[column+1] + row+2[column+2]
with row incrementing by 1 from 0 to 6
and column incrementing by 1 from 0 to 6.
"""


def hourglassSum(arr):
    hourglass_sum = float('-inf')

    for row in range(4):
        for column in range(4):
            hourglass_sum = sum([arr[row][column],
                                 arr[row][column+1],
                                 arr[row][column+2],
                                 arr[row+1][column+1],
                                 arr[row+2][column],
                                 arr[row+2][column+1],
                                 arr[row+2][column+2]])
            if hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = hourglass_sum
    return max_hourglass_sum


matrix = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

print(matrix[0][0])

print(hourglassSum(matrix))
