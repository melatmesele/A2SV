class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        dic = {'a' ,'e' ,'i' , 'o' , 'u'}
        bcount = 0
        right = 0
        # arr = []
        while right < k:
            # arr.append(s[right])
            if s[right] in dic:
                bcount += 1
            right += 1
        acount = bcount
        maxcount = bcount
        left = 0
        while right < len(s):
            if s[left] in dic:
                acount -= 1
            if s[right] in dic:
                acount += 1
            left += 1
            right += 1
            maxcount = max(maxcount , acount)
        return maxcount
            
        