def is_valid(number: int) -> bool:
    """Check whether number is valid 4-digit number"""
    if not isinstance(number, int):
        print("Your input is not number, please input number")
        return False
    if number not in range(1000, 10000):
        print("Please input 4-digit number")
        return False
    if not is_digits_different(number):
        print("Please input number with different digits")
        return False

    return True


def is_digits_different(number: int) -> bool:
    """Check if all digits are different by pairs"""
    str_number = str(number)
    for digit in str_number:
        if str_number.count(digit) > 1:
            return False

    return True
