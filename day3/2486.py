from typing import List

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # 2ptr approach. basically keep two vars to track the pos in both the strings
        # both start from index 0
        s1, t1 = 0, 0

        # loop to check if one of the ptr reaches the end of the string
        while s1 < len(s) and t1 < len(t):
            # if char is a match then increment pointers
            if s[s1] == t[t1]:
                s1, t1 = s1+1, t1+1
            else:
                # else increment original string ptr
                s1+=1
        # return length of t minus pointer index from where the subsequence has to be added
        return len(t) - t1