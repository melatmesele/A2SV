class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []
        if len(s)== 1 and s[0]=="*":
            return ""
        for i in s:
            
            if i != "*":
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)
        
    
    
        