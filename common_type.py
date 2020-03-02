
def get_common_type(type1: type, type2: type) -> type:
    types = {1: bool, 2: int, 3: float, 4: complex, 5: range, 6: tuple, 7: list, 8: str}
    """if type1 == str:
        return str
    elif type1 == list:
        return list
    elif type1 == float:
        return float
    elif type1 == complex:
        return complex
    elif type1 == range:
        return range
    elif type1 == tuple:
        return tuple
    elif type1 == bool:
        return bool
    elif type1 == int:
        return int

    if type2 == str:
        return str
    elif type2 == list:
        return list
    elif type2 == float:
        return float
    elif type2 == complex:
        return complex
    elif type2 == range:
        return range
    elif type2 == tuple:
        return tuple
    elif type2 == bool:
        return bool
    elif type2 == int:
        return int
"""
    for key in types:
        if type1 == key:
            return key
        if type2 == key:
            return key
    """
    Calculate common type according to rule, that it must have the most adequate interpretation after conversion.
    Look in tests for adequacy calibration.
    :param type1: one of [bool, int, float, complex, list, range, tuple, str] types
    :param type2: one of [bool, int, float, complex, list, range, tuple, str] types
    :return: the most concrete common type, which can be used to convert both input values
    """
