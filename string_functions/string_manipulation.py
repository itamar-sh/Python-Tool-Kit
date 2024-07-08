class StringManipulation:
    def convert_string_into_zigzag(self, text, numRows):
        """
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

        P   A   H   N
        A P L S I I G
        Y   I   R
        And then read line by line: "PAHNAPLSIIGYIR"

        Write the code that will take a string and make this conversion given a number of rows:

        string convert(string s, int numRows);
        Example 1:
        Input: s = "PAYPALISHIRING", numRows = 3
        Output: "PAHNAPLSIIGYIR"

        Example 2:
        Input: s = "PAYPALISHIRING", numRows = 4
        Output: "PINALSIGYAHRPI"
        Explanation:
        P     I    N
        A   L S  I G
        Y A   H R
        P     I
        """
        if numRows == 1:
            return text
        result_pattern = [""] * numRows
        for i in range(len(text)):
            round_size = 2 * numRows - 2
            # check row of letter
            char_location_in_round = i % round_size
            if (char_location_in_round) < numRows:
                result_pattern[char_location_in_round] += text[i]
            else:
                result_pattern[round_size - char_location_in_round] += text[i]
        return "".join(result_pattern)

    def convert_roman_to_int(self, text):
        """
        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        For example, 2 is written as II in Roman numeral, just two ones added together.
        12 is written as XII, which is simply X + II.
        The number 27 is written as XXVII, which is XX + V + II.
        Roman numerals are usually written largest to smallest from left to right.
        However, the numeral for four is not IIII.
        Instead, the number four is written as IV.
        Because the one is before the five we subtract it making four.
        The same principle applies to the number nine, which is written as IX.
        There are six instances where subtraction is used:
        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.
        Given a roman numeral, convert it to an integer.
        """
        letters_to_value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        for char_index in range(len(text)):
            if char_index > 0 and letters_to_value[text[char_index]] > letters_to_value[text[char_index-1]]:
                num += letters_to_value[text[char_index]] - 2 * letters_to_value[text[char_index-1]]
            else:
                num += letters_to_value[text[char_index]]
        return num