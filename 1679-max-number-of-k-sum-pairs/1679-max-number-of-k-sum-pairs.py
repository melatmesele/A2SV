class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        start,end = 0, len(nums)-1
        result = 0
        while start<end:
            sums = nums[start]+nums[end]
            if (sums == k):
                result+=1
                start+=1
                end-=1
            elif(sums<k):
                start+=1
            else:
                end-=1
        return result
        