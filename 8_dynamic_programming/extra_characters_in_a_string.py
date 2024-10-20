from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_bag = set(dictionary)
        word_bag.add("")  # for inserting the basic case each time
        dt = [0]
        for char_index in range(1, len(s)+1):
            min_remain = char_index
            for location, previos_remain in enumerate(dt):
                word_to_complete = s[location:char_index]
                for word in word_bag:
                    if word in word_to_complete:
                        min_remain = min(min_remain, len(word_to_complete) - len(word) + previos_remain)
            dt.append(min_remain)
        return dt[-1]
