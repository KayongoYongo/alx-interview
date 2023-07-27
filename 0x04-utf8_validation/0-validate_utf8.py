#!/usr/bin/python3
"""
This function carries out a UTF-8 validation of numbers.
If they are UTF-8 comploiant, the function returns True.Else,
it returns false
"""


def validUTF8(data):
    """
    This function carries out UTF-8 validation.

    Args: data - This is the array that will be queried by the function

    Return: True if it is UTF-8 compliant system,
            False if it is not complint
    """
    def get_num_bytes(byte):
        """
        This function gets the number of bytes in an integer.

        Args: byte - This is the integer to be quried.

        Return: An integer value:
        """
        if byte >> 7 == 0b0:
            return 1
        elif byte >> 5 == 0b110:
            return 2
        elif byte >> 4 == 0b1110:
            return 3
        elif byte >> 3 == 0b11110:
            return 4
        else:
            return 0

    def is_continuation(byte):
        """
        This function queries the next integer in the list

        Args: byte-The next integer to be queried
        """
        return byte >> 6 == 0b10

    index = 0
    while index < len(data):
        num_bytes = get_num_bytes(data[index])
        if num_bytes == 0:
            return False

        for i in range(1, num_bytes):
            if index + i >= len(data) or not is_continuation(data[index + i]):
                return False

        index += num_bytes

    return True
