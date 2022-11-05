class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums,l,h):
            while l<=h:
                nums[l],nums[h] = nums[h],nums[l]
                l+=1
                h-=1
        
        n = len(nums)
        k = k%n
        reverse(nums,0,n-k-1)
        reverse(nums,n-k,n-1)
        reverse(nums,0,n-1)
        