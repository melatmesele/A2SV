class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        right = 0
        left = 0 
        minn = float('INF')
        array = []
        nums.sort()
        if k == 1:
            return 0
        while right <= len(nums):
            if right < k:
                array.append(nums[right])
            
            else:
                diff = max(array) - min(array)
                minn = min(diff , minn)
                array.remove(nums[left])
                if right < len(nums):
                    array.append(nums[right])
               
                left += 1
            right += 1
        return minn
                
                
                
            
        
        
        
        # minn = float('INF')
        # if k == 1:
        #     return 0
        # for i in range(len(nums)):
        #     for j in range(i+1 ,len(nums)):
        #         diff = abs(nums[i]  - nums[j])
        #         minn = min(diff , minn)
        # return minn
        