def is_palindrome(value: str) -> bool:
    new_value = value.lower()
    new_value2 = new_value.replace(" ", "")
    if new_value2 == new_value2[::-1]:
        return True
    else:
        return False

    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """

