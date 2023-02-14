class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])
        minimum = min(prefixSum)
        if minimum >= 1:
            return 1
        return abs(minimum)+1
                  #### brute force       
      # for i in range(1, len(nums)*100 +1):
#             result= i
#             flag = True
            
#             for j in range(len(nums)):
#                 result +=  nums[j]
#                 if result  < 1:
#                     flag = False
#                     break
#             if flag == True: 
#                 return i

                 ### optimized
    
            
        
                