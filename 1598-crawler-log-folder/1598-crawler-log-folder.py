class Solution:
    def minOperations(self, logs: List[str]) -> int:
        m = "../"
        n = "./"
        stack1 =[]
        for i in logs:
            if i == m :
                if len(stack1) > 0:
                    stack1.pop()
            elif i == n:
                continue
            else:
                stack1.append(i)
        return len(stack1)
        