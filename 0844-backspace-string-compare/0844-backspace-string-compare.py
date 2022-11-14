class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        # s = "ab#c", t = "ad#c"
              # ac         ac
        # s = "##b#"   t = "b#"
             
        stack1 = []
        stack2 =[]
        for  i in range(len(s)):
            
            if s[i] == "#" and len(stack1)== 0:
                continue
            elif s[i] == "#" and stack1:
                
                stack1.pop()
            else:
                 stack1.append(s[i])
        for  j in range(len(t)):
            if t[j] == "#" and len(stack2)== 0:
                continue
            elif t [j] == "#" and stack2:
                stack2.pop()
            else:
                 stack2.append(t[j])
        return True if stack1 == stack2 else False
        
                