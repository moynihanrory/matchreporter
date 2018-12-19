import matchreport.constants

def removePrefix(str, prefix):
    if str.startswith(prefix):
        return str[len(prefix):]
    else:
        return str

def parseInt(s, stripPrefix=False):
    try:
        if (stripPrefix):
            return int(eval(str(removePrefix(s, src.constants.TIME_HELPER_STR_ZERO))))
        else:
            return int(eval(str(s)))
    except:
        return 0

def getTimeBucket(time, half):
    halfInt = parseInt(half)

    minString = time

    minInt = parseInt(minString)

    x = divmod(minInt, 10)
    sector = x[0]

    if halfInt == 1:
        if sector > 2:
            bucketInt = 2
        else:
            bucketInt = sector
    else:
        if sector > 5:
            bucketInt = 5
        else:
            bucketInt = sector

    return bucketInt


