class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        ans = 1
        left  = 0
        nums.sort()
        
        for right in range(1 , len(nums)):
            
            while (right - left)*(nums[right] - nums[right-1]) > k:
                k +=  nums[right-1] - nums[left]
                left += 1
            
            ans = max(ans , right-left+1)
            k -= (right - left)*(nums[right] - nums[right-1])
        return ans