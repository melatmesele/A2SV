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
            
            
                    
                    
            
                  