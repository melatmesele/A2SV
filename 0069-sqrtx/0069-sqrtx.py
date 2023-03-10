class Solution:
    def mySqrt(self, x: int) -> int:
        
        left = 1
        right = x
        if x == 0:
            return 0
        result = inf
        while(left <= right):
            mid = left + (right -left)//2
                
            if mid*mid <=  x:
                result = mid
                left = mid + 1
        
            elif mid*mid > x:
                right = mid -1
        return result
                
                
        