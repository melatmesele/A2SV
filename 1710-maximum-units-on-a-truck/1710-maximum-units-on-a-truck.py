class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1] , reverse = True)
        res = 0
        for box , unit in boxTypes:
            if truckSize < box:
                return res + truckSize * unit
            res+= box *unit             
            truckSize-=box
        return res
# #         [[1,3],[2,2],[3,1]]
# #           1*3      1*2      2*1 total =7
# #           1*3     2*2  1*1   total = 8
        
#         [[5,10],[2,5],[4,7],[3,9]],  s = 10
#           5*10 + 3*7 + 1*9  +1 *5 =50+21+9+5 = 85
#             50 + 27 +14
          
                
#         boxTypes.sort(key=lambda x: x[1], reverse=True)
#         res = 0
#         for n, units in boxTypes:         ,[5,10]  [3,9] ,[4,7] ,  [2,5] 
#                                             50+ 27+14
       
                                            
                           
                                            
#             if truckSize < n:
#                 return res + units*truckSize
#             res += units * n  
#             truckSize -= n    
        
#         return res
            