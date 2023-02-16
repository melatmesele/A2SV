class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        ans = []
        summ = 0
        for right in range(len(nums)):
            if right - left + 1 < k:
                summ += nums[right]
            elif right- left + 1 >= k:
                summ += nums[right]
                ans.append(summ)
                summ -= nums[left]
                
                left += 1
        return max(ans)/k
                
             
            
#         right =0 
#         left = 0
#         summ = 0
       
#         result = []
#         while right < k:
#             summ += nums[right]
#             right += 1
#         result.append(summ)
#         while right < len(nums):
#             summ += nums[right]
#             summ -= nums[left]
#             result.append(summ)
#             left += 1
#             right += 1
#         return max(result) /k
            
            
            
            
        