class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        back =  len(nums)-1
        result = []
        while(back >= left):
            if abs(nums[left]) >= abs(nums[back]):
                result.append(nums[left]**2)
                left += 1
            else:
                result.append(nums[back]**2)
                back -= 1
        result.reverse()
        return result
            
                
        
       