from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 2ptr approach. start at start, end at end of the list/string-char array
        # swap start char with end char and increment start by 1 and decrement end by 1
        start, end = 0, len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1
        