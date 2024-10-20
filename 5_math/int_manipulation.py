import pytest


class IntManipulation:
    def reverse_32_int(self, num):
        """
        Given a signed 32-bit integer x, return x with its digits reversed.
        If reversing x causes the value to go outside the signed 32-bit integer
        range [-231, 231 - 1], then return 0. Assume the environment does not
        allow you to store 64-bit integers (signed or unsigned).
        """
        INT_MAX = 0x7FFFFFFF  # 2147483647
        # We dont afraid of the reversed of INT_MIN since it bigger than 32-bit

        result = 0
        sign = 1 if num >= 0 else -1
        num = abs(num)
        while num != 0:
            digit = num % 10
            if result > (INT_MAX - digit) // 10:
                return 0
            result = result * 10 + digit
            num = num // 10
        return result * sign

@pytest.mark.parametrize("input, expected_output, test_name",[
    (123456789, 987654321, "positive number"),
    (0, 0, "zero"),
    (-123, -321, "negative number"),
    (2147483647, 0, "Overflow case: max value"),
    (-2147483648, 0, "Overflow case: min value"),
])
def test_reverse_32_int(input, expected_output, test_name):
    assert IntManipulation().reverse_32_int(input) == expected_output, test_name