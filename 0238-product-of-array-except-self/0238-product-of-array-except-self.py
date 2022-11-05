class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)   # res => [1 , 1, 1, 1]
        prefix = 1 
        postfix = 1

        for i in range(len(nums)) :  # [1,2,6,24]
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1 , - 1 , - 1) :  # [24,24,12,4]
            res[i] *= postfix
            postfix *= nums[i]
        return res
        