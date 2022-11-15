class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        ans = [0]*len(nums)
        c = len(nums) - 1
        d = 0
        for i in range(len(nums)):
            if nums[i] %2 != 0 :
                ans[c] = nums[i]
                c-=1
            else:
                ans[d] = nums[i]
                d+=1
        return ans 
                
                
        