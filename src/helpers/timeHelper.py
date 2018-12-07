import src.constants

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
        return


def getTimeBucket(time, half):
    colonIndex = time.find(src.constants.TIME_HELPER_STR_COLON)

    if (colonIndex <= 0): #android format
        bucketString = time[:colonIndex]

        if (bucketString == src.constants.TIME_HELPER_STR_ZERO):
            bucketInt = src.constants.TIME_HELPER_INT_ZERO
        else:
            bucketInt = parseInt(bucketString, True)

        if (half == src.constants.TIME_HELPER_INT_ONE):
            return bucketInt
        else:
            return bucketInt + src.constants.TIME_HELPER_INT_SECTOR_PER_HALF
    else: # ios format
        bucketString = time[:colonIndex]

        halfInt = parseInt(half)

        bucketInt = parseInt(bucketString)

        # int must be 0 5
        if (bucketInt < 10):
            bucketInt = 0

            if (halfInt == src.constants.TIME_HELPER_INT_ONE):
                return bucketInt
            else:
                return bucketInt + src.constants.TIME_HELPER_INT_SECTOR_PER_HALF
        else:
            x = divmod(bucketInt, 10)

            if (halfInt == src.constants.TIME_HELPER_INT_ONE):
                if (x[0] > src.constants.TIME_HELPER_INT_TWO):
                    return src.constants.TIME_HELPER_INT_TWO
                else:
                    return x[0]
            else:
                if (x[0] > src.constants.TIME_HELPER_INT_TWO):
                    return src.constants.TIME_HELPER_INT_SECTOR_LAST_POS
                else:
                    return x[0] + src.constants.TIME_HELPER_INT_SECTOR_PER_HALF

