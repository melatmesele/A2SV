class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # nums.sort()
        # # [5,3,6,1,12]      1 ,3 ,5 ,6,12
        # while(original in nums):
        #     original *= 2
        # return original
        nums.sort()
        
        for n in nums:
            if original == n:
                original*=2
        return original
        
            
                        
        
        