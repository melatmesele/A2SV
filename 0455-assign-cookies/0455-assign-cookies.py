class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g = [1,2], s = [1,2,3]
        # g= [1,2,3], s = [1,1]
        # counter = 1 + 1
        # counter = 1
        g.sort()
        s.sort()
        len_s = len(s) - 1
        counter = 0
        for i in range(len(g)-1 , -1 , -1):
            if len_s < 0:
                break
            if s[len_s] >= g[i]:
                len_s -=1
                counter+=1
        return counter
        
        
#         
        
        
        
        
        
        
        
        
        
#         #         cookie = [1 ,2 ,3]  [1 ,2 ,3]
# #         child = [1 ,2]       2 ,1
#         g,s = sorted(g), sorted(s)
        
#         lg, ls = len(g), len(s)
        
#         sp = ls-1
#         ans = 0
#                       # 2,-1,-1
#         for i in range(lg-1, -1, -1):
            
#             if sp < 0:
#                 break
            
#             if s[sp] >= g[i]:
#                 ans += 1
#                 sp-=1                

#         return ans
        
        
        
        # cookie = [1 ,1]
        # child = [1 ,2, 3]     child 1 wants 1 cookie   satisfied 
        #                       child 2 wants 2 cookie   not satisfied
        #                       child 3 wants 3 cookie   not satisfied
#                 # brute force
#         counter = 0
#         for i in g:
#             for j in s:
#                 if i <= j:
#                     counter+=1
#                     break
#         return counter
                        
                
        
                
                
            
        