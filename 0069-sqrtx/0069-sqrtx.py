class Solution:
    def mySqrt(self, x: int) -> int:
        
        left = 1
        right = x
        if x == 0:
            return 0
        result = inf
        while(left <= right):
            mid = left + (right -left)//2
            if mid*mid == x:
                return mid
            elif mid*mid <  x:
                result = mid
                left = mid + 1
        
            else:
                right = mid - 1
                result = mid - 1
        return result
                
                
        