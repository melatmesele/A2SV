class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        product = 1
        counter = 0
        if k == 0 or k == 1:
            return 0
        while right < len(nums):
            product *= nums[right]
            while product >= k:
                product /= nums[left]
                left += 1
            
            counter += right - left + 1
            right += 1
        return counter
        
        