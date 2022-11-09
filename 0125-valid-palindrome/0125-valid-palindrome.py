class Solution:
    def isPalindrome(self, s: str) -> bool:
        strr = ""
        for n in s:
            if n.isalnum():
                
                strr+= n.lower()
        left, right = 0 , len(strr)- 1
        while(left < right):
            if strr[left] != strr[right]:
                return False
            else:
                left += 1
                right -= 1
        return True        
            
        