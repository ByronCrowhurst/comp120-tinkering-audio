def is_odd(number_to_check):
    """
    Checks to see if a number is odd or even
    Divides a number by 2 and checks to see if the float version and integer version are the same.

    :param number_to_check:     Number that is being checked.
    :return:                    True if the number is odd, False if the number is even.
    """
    number_to_compare = int(number_to_check / 2)
    number_to_check = float(number_to_check / 2)
    if number_to_check != number_to_compare:
        return True
    else:
        return False
