class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        for r in range(len(nums)):
            
            # if nums[r]==0:
            #     l = r + 1
            #     # nums[r] = 1
            while nums[r] == 0:
                l  = r + 1
                break
            # if r < len(nums):
            ans = max(ans , r - l + 1)
        return ans
        