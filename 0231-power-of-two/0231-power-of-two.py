class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        counter = 1
        if n == 1 :
            return True
        
        if n <= 0:
            return False
        if n %2 != 0 :
            return False
        return self.isPowerOfTwo(n / 2)
    
    
#     if n == 1 or n == -1:
#             if counter % 2 == 0:
#                 return True
#             else:
#                 return False
        
#         if n < 0:
#             # n = -n
#             counter += 1