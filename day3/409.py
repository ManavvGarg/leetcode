class Solution:
    def longestPalindrome(self, s: str) -> int:
        # init a set to keep track of variables
        o = set()

        # pL for palindromeLength
        pL = 0

        # iterate over the string to get each char
        for ch in s:
            # if char in set remove char from set and add 2 to pL (palindrome formed from 2 same chars, a____a, [2 a's])
            if ch in o:
                o.remove(ch)
                pL+=2
            else:
                # else add the char in set
                o.add(ch)

        # if any chars are left in the set, we can increment pL with 1 cause a palindrome can have one and only one char with no pair in the middle, so it doesnt matter how many chars are left, it can 100 or it can 1 or something else
        if len(o) >= 1:
            pL += 1
        
        return pL
