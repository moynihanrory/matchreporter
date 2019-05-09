
def getTimeSector(time, half):
    x = divmod(time, 10)
    bucket = x[0]

    if bucket > 2:
        sector = 2
    else:
        sector = bucket

    if half is 2:
        sector = sector + 3

    return sector
