""".py file for 4-digit number game"""
import random
from utils import is_valid


# generating 4 digits for number
first_digit = random.randint(1, 9)  # generate first digit
available_digits_list = list(range(10))
available_digits_list.remove(first_digit)

actual_digits = [first_digit]
while len(actual_digits) != 4:
    digit = random.choice(available_digits_list)
    actual_digits.append(digit)
    available_digits_list.remove(digit)


COUNTER_OF_MATCHING_DIGITS = 0
while COUNTER_OF_MATCHING_DIGITS != 4:
    # handling problems with input errors
    try:
        input_number = eval(input("input your number: "))
    except Exception:
        print("Please input valid number")
        input_number = eval(input("input your number: "))

    # validate input number
    while not is_valid(input_number):
        # handling problems with input errors
        try:
            input_number = eval(input())
        except Exception:
            print("Please input valid number")
            input_number = eval(input("input your number: "))

    input_digits = [int(i) for i in str(input_number)]

    COUNTER_OF_DIGITS = 0
    COUNTER_OF_MATCHING_DIGITS = 0
    for act, pred in zip(actual_digits, input_digits):
        if pred in actual_digits:
            COUNTER_OF_DIGITS += 1
        if act == pred:
            COUNTER_OF_MATCHING_DIGITS += 1

    print(f"{COUNTER_OF_DIGITS} : {COUNTER_OF_MATCHING_DIGITS}")

print("Congratulations. You win!!")
