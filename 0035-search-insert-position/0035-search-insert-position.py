class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
#         left = 0
#         right = len(nums)-1
#         result = inf
#         while(left <= right and right >=0):
            
#             mid = left + (right - left)//2
            
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid + 1
#                 result = mid + 1
#             else:
#                 right = mid -1
#                 result = mid
#         return result
            
        
        
        
        
        
        left= 0
        right = len(nums) - 1
        result = 0 
        
        while(left <= right and right >= 0):
            
            mid = left +  (right- left)// 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                result = mid + 1
                left = mid + 1
            else:
                result = mid 
                right = mid - 1
        return result
                
        

                