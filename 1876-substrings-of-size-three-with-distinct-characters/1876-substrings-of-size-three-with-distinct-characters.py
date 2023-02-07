class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        counter = 0 
        left = 0
        right = 2
        while(right < len(s)):
            dicti = {}
            for i in range(left , right+1):
                
                dicti[s[i]] = 1
            if len(dicti) == 3:
                counter +=1
            left +=1
            right += 1
        return counter
        