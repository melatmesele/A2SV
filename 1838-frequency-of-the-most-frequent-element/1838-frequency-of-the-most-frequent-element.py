class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        left = 0
        right = 1
        counter = 1
        result = 1
        nums.sort()
        while right < len(nums):
            diff = (right - left)*(nums[right] - nums[right-1])
            if diff <= k:
                counter += 1
                right += 1
                k -= diff
            else:
                k +=(nums[right-1] - nums[left])
                left += 1
                counter -= 1
            result = max(result , counter)
        return result
        
                
        