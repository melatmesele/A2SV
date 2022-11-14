class Solution:
    def makeGood(self, s: str) -> str:
        # s = "leEeetcode"
                 
        #      leetcode
        # stack=[leetcode]
        # s = "abBAcC" 
        #      aAcC
        # stack=[c
        #      cC
        stack=[]
        for i in range(len(s)):
            if  not stack:
                stack.append(s[i])
            elif stack[-1].isupper() and stack[-1].lower() == s[i]:
                stack.pop()
            elif stack[-1].islower() and stack[-1].upper() == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
            
            
            
            
            
            
            
      