class Solution:
    def minStartValue(self, nums: List[int]) -> int:
       
        for i in range(1, len(nums)*100 +1):
            result= i
            flag = True
            
            for j in range(len(nums)):
                result +=  nums[j]
                if result  >= 1:
                    
                    continue
                else:
                    flag = False
                    break
            if flag == True: 
                return i
            
        
                