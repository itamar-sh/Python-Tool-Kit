class Palindrom:
    def is_palindrom(self, num: int):
        # palindrome is not negative and can't end with 0
        if num < 0 or (num > 0 and num % 10 == 0):
            return False

        half_num_reverted = 0
        temp_num = num
        while temp_num > half_num_reverted:
            half_num_reverted = half_num_reverted * 10 + temp_num % 10
            temp_num //= 10

        return temp_num == half_num_reverted or temp_num == (half_num_reverted // 10)