class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        min = nums[0] * nums[1]
        max = nums[-1] * nums[-2]
        return max - min
        

        # nums = [5,6,2,7,4]
        #         i          
        #              j
#         brute force
#                 max = nums[0] * nums[1]
#                 min = nums[0] * nums[1]
#                 for i in range(len(nums)-1):
#                     for j in range(len(nums)):
                    
#                         if i == j:
#                             continue
#                         else:    
#                             prod = nums[i] *nums[j]
#                             if prod > max:
#                                 max = prod
#                             if prod < min:
#                                 min = prod
#                 return max - min


                
                    