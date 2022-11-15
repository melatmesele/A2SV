class Solution:
    def climbStairs(self, n: int) -> int:
        stack1 = []
        for i in range(n+1):
            if i == 0 or  i== 1:
                stack1.append(1)
            else:
                stack1.append(stack1[-1] + stack1[i-2])
                
        return stack1[-1]
	    