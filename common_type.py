def get_common_type(type1: type, type2: type) -> type:
    if type1 == str:
        return str

    if type1 == bool:
        return type2

    if type1 == type2:
        return type1

    if type1 == list and type2 == range or type2 == tuple:
        return list
    else:
        return str

    if type1 == range:
        return str

    if type1 == float and type2 == complex:
        return complex

    if type2 == complex:
        return complex
    else:
        return int





"""
    Calculate common type according to rule, that it must have the most adequate interpretation after conversion.
    Look in tests for adequacy calibration.
    :param type1: one of [bool, int, float, complex, list, range, tuple, str] types
    :param type2: one of [bool, int, float, complex, list, range, tuple, str] types
    :return: the most concrete common type, which can be used to convert both input values
"""
