def validate_owner(value):
    if not isinstance(value, str):
        raise TypeError("owner must be string")
    if not value.strip():
        raise ValueError("owner empty")
    return value.strip()


def validate_price(value):
    if not isinstance(value, (int, float)):
        raise TypeError("price must be number")
    if value <= 0:
        raise ValueError("price must be >0")
    return value


def validate_money(value):
    if not isinstance(value, (int, float)):
        raise TypeError("money must be number")
    if value < 0:
        raise ValueError("money must be >=0")
    return value


def validate_term(value):
    if not isinstance(value, int):
        raise TypeError("term must be int")
    if value <= 0:
        raise ValueError("term must be >0")
    return value


def validate_bool(value):
    if not isinstance(value, bool):
        raise TypeError("must be bool")
    return value