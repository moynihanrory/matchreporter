from matchreporter.constants import STRING_ZERO


def removePrefix(str, prefix):
    if str.startswith(prefix):
        return str[len(prefix):]
    else:
        return str


def parseInt(s):
    try:
        return int(eval(str(removePrefix(s, STRING_ZERO))))
    except:
        return 0


def stripAndConvertTimeToInt(stringValue):
    i = 0
    stopIndex = 0

    if ':' in stringValue:
        stopIndex = stringValue.find(':')
    else:
        stopIndex = stringValue.find('m')

    return stripAndConvertToInt(stopIndex, stringValue)


def stripAndConvertHalfToInt(stringValue):
    i = 0
    stopIndex = 0

    if '1' in stringValue:
        stopIndex = stringValue.find('s')
    else:
        stopIndex = stringValue.find('n')

    return stripAndConvertToInt(stopIndex, stringValue)


def stripAndConvertToInt(stopIndex, stringValue):
    subStringValue = stringValue[0:stopIndex]

    return parseInt(subStringValue)