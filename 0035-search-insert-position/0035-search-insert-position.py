class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        result = inf
        while(left <= right and right >=0):
            
            mid = left + (right - left)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                result = mid + 1
            else:
                right = mid -1
                result = mid
        return result
            
#             if left == len(nums)-1 and nums[left]< target:
#                 return left + 1
#             elif left == len(nums)-1 and nums[left] > target:
#                 return left 
#             elif  right  ==0 and nums[left] > target:
#                 return left 
#             elif right  ==0  and nums[left] > target:
#                 return left 
#             elif nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid +1
#             elif nums[mid] > target:
#                 right = mid - 1
            
        
                