from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        listToPrint = []

        # create a hash map of all the chars in the first word of the list
        cnt = Counter(words[0])

        # save one iteration
        words.pop(0)

        # for word in words
        for w in words:
            # create a hash map for the current word with count of all chars
            word_cnt = Counter(w)
            # for char in a hashmap cnt(cause thats the base word and words which have common chars with the first are valid)
            for c in cnt:
                # get the count of char in cnt and count of char in word_Cnt and minmize it. this way we know the min occurance of the char if it exists.
                # store the min value in first word dict, cause we can just use the first word dict to make our result list and save time plus operations
                # beautiful thing about Counter is, if 'c' char doesnt exist, then it becomes a default dict -> which returns 0. so no errors. Ex:- min(4, NULL) becomes -> min(4, 0) which returns 4 and no errors
                cnt[c] = min(cnt[c], word_cnt[c])
        
        # for every key in  first word dict
        for key in cnt:
            # for keyCount in range the amount of times that key (char) is
            for keyCount in range(cnt[key]):
                # append the char that many times in resultant list
                listToPrint.append(key)
        
        return listToPrint