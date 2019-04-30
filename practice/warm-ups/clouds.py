def jumpingOnClouds(c):
    num_clouds = len(c)
    min_jumps = 0
    position = 0
    while position < num_clouds:
        if position + 2 < num_clouds and c[position + 2] == 0:
            position += 2
        else:
            position += 1
        if position != num_clouds:
            min_jumps += 1
    return min_jumps


def jumpingOnCloudsTwo(c):
    last_cloud = len(c) - 1
    min_jumps = 0
    position = 0
    while position < last_cloud:
        if position + 2 < last_cloud and c[position + 2] == 0:
            position += 2
        else:
            position += 1
        min_jumps += 1
    return min_jumps


print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))  # 4
print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))  # 3
print(jumpingOnClouds([0, 0, 1, 0, 0, 0, 0, 1, 0, 0]))  # 6


print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))  # 4
print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))  # 3
print(jumpingOnClouds([0, 0, 1, 0, 0, 0, 0, 1, 0, 0]))  # 6