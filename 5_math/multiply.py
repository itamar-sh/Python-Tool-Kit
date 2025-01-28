"""
Given two numbers return their multiply result without arithemetic operation
"""

def multiply(num1, num2):
    sign = 1
    if num1 < 0:
        sign *= -1
        num1 = abs(num1)
    if num2 < 0:
        sign *= -1
        num2 = abs(num2)
    if num2 > num1:
        num1, num2 = num2, num1

    result = 0
    while num2 != 0:
        if num2 & 1:
            result += num1
        num1 = num1 << 1
        num2 = num2 >> 1
    return result



# Example usage
print(multiply(1000, 1000))  # Should return 1000000
print(multiply(-1000, 1000))  # Should return -1000000
print(multiply(10000, 10000))  # Should return 
print(multiply(50000, 50000))  # Should return 











from ctypes import c_int32

def multiply_ctype(num1: c_int32, num2: c_int32):
    sign = c_int32(1)
    if num1.value < c_int32(0).value:
        sign.value = sign.value*c_int32(-1).value
        num1.value = num1.value*c_int32(-1).value
    if num2.value < c_int32(0).value:
        sign.value = sign.value*c_int32(-1).value
        num2.value = num2.value*c_int32(-1).value
    # Access the actual integer value using the `.value` attribute
    if num2.value > num1.value:  # Always ensure num2 is the smaller number
        num1, num2 = num2, num1


    result = c_int32(0)
    # Perform multiplication using bit manipulation or addition
    while num2.value != 0:
        if (num2.value & 1) != 0:  # Check if the least significant bit is set
            result = c_int32(result.value + num1.value)

        num1 = c_int32(num1.value << 1)  # Shift num1 left by 1 (multiply by 2)
        num2 = c_int32(num2.value >> 1)  # Shift num2 right by 1 (divide by 2)

    return result.value*sign.value

# Example usage
print(multiply_ctype(c_int32(-1000), c_int32(-1000)))  # Should return 1000000
print(multiply_ctype(c_int32(-1000), c_int32(1000)))  # Should return -1000000
print(f"1000*1000={1000*1000} and indeed our function return: {multiply_ctype(c_int32(1000), c_int32(1000))}")
print(f"10000*10000={10000*10000} and indeed our function return: {multiply_ctype(c_int32(10000), c_int32(10000))}")
print(multiply_ctype(c_int32(50000), c_int32(50000)))  # Overflow

