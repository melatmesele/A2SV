class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
    #     left=2 right = 5
    #     2  3 4 5
    #             ranges =  [1,2] , [3,4] , [5,6] , 
    #                2
    #                       3
    #                       4
    #                               5  
#                 for i in range(left , right+1):
#                     for j in range(len(ranges)):
#                         ans = False
#                         if i >= ranges[j][0] and i <= ranges[j][1]:
#                             ans = True
#                             break
#                 return ans  

          # left=2 right = 5
    #     2  3 4 5  summ = 14
    #             ranges =  [1,2] , [3,4] , [5,6] ,
                            # 1   2 
        summ = sum(range(left , right+1))
        for i in range(left, right+1):
            
            for j in ranges:
                if i >= j[0] and  i <= j[1]:
                    summ -= i
                    break
       
        return summ == 0
                


            
        

                        