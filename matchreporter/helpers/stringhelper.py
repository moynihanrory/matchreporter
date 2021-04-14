from matchreporter.constants import STRING_ZERO


def remove_prefix(prefixed, prefix):
    if prefixed.startswith(prefix):
        return prefixed[len(prefix):]

    return prefixed


def parse_int(int_str):
    try:
        return int(eval(str(remove_prefix(int_str, STRING_ZERO))))
    except:
        return 0


def strip_and_convert_time_to_int(string_value):
    if ':' in string_value:
        stop_index = string_value.find(':')
    else:
        stop_index = string_value.find('m')

    return strip_and_convert_to_int(stop_index, string_value)


def strip_and_convert_half_to_int(string_value):
    if '1' in string_value:
        stop_index = string_value.find('s')
    else:
        stop_index = string_value.find('n')

    return strip_and_convert_to_int(stop_index, string_value)


def strip_and_convert_to_int(stop_index, string_value):
    sub_string_value = string_value[0:stop_index]

    return parse_int(sub_string_value)
