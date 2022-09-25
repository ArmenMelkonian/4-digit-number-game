import random
from utils import is_valid


# generating 4 digits for number
first_digit = random.randint(1, 9)  # generate first digit
available_digits_list = [i for i in range(10)]
available_digits_list.remove(first_digit)

actual_digits = [first_digit]
while len(actual_digits) != 4:
    digit = random.choice(available_digits_list)
    actual_digits.append(digit)
    available_digits_list.remove(digit)


counter_of_matching_digits = 0
while counter_of_matching_digits != 4:
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

    counter_of_digits = 0
    counter_of_matching_digits = 0
    for act, pred in zip(actual_digits, input_digits):
        if pred in actual_digits:
            counter_of_digits += 1
        if act == pred:
            counter_of_matching_digits += 1

    print(f"{counter_of_digits} : {counter_of_matching_digits}")

print("Congratulations. You win!!")
