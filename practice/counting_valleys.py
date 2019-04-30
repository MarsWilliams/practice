def countingValleys(n, s):
    valleys = 0
    altitude = 0
    for step in s:
        if step == 'U':
            altitude += 1
        if step == 'D':
            altitude -= 1
        if altitude == 0 and step == 'U':
            valleys += 1
    return valleys
