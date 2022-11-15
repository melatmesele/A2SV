class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
#        names = ["Mary","John","Emma"], heights = [180,165,170]
#        names2 =[    "Mary"     , "Emma"   , "John"      ]   
                                       
#                                        heights2 = [165 , 170 ,180]  
# [180,165,170]
# 165 180 ,170


        heights2 = sorted(heights)
        new_names=[0]*len(heights)
        for i in range(len(heights)):
            new_names[i] =names[heights.index(heights2[-1-i])]
        return new_names

#                       using hash map
        
#         dic = {}
#         ans = []
#         for idx , height in enumerate(heights):
#             dic[height] = names[idx]
#         heights.sort(reverse=True)     
#         # heights = [180 , 170 ,165]
#         for  height in heights:
#             ans.append(dic[height])
        
#         return ans
        
    
    
    
    
        
        
#         d = {}
#         for idx, height in enumerate(heights):
#             d[height] = names[idx]
        
#         heights.sort(reverse=True)
        
#         res = []
#         for height in heights:
#             res.append(d[height])
        
#         return res
            
                    
                    
            
                  