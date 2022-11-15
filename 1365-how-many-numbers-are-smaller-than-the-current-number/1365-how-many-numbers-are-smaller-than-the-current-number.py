class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        new = sorted(nums)
        for i in range(len(nums)):
            ans[i] = new.index(nums[i])
        return ans
        
        # nums = [ 8 ,1 ,2 , 2, 3]
        # new = [ 1 ,2 ,2 ,3 ,8]
#         ans=  [4 ,0 ,1 ,1 ,3]
       
    
#     new=sorted(nums)
#     n=len(nums)
#     ans=[0]*n
    
#     for i in range(n):
#         ans[i]=new.index(nums[i])
#     return ans    
        
        
        
        
        
        
        
        
        
        
    
#         brute force
#         ans = []
        
#         for i in range(len(nums)):
#             counts = 0
#             for j in range(len(nums)):
#                            if nums[i] > nums[j]:
#                                 counts+=1
#             ans.append(counts)
#         return ans
