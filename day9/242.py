class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dick = {}
        dick2 = {}
        for i in s:
            if i in dick:
                dick[i] += 1
            else:
                dick[i] = 1
        
        for i in t:
            if i in dick2:
                dick2[i] += 1
            else:
                dick2[i] = 1
            
        return (dick == dick2)