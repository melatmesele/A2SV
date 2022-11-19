class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # count_glass, count_paper,count_metal = 0 , 0 ,0
        # idx_glass, idx_paper,idx_metal = 0 , 0 ,0
        time = []
        time.append(0)
        for i in range(len(travel)):
            time.append(time[-1] + travel[i])
        result = 0
        for j in ["M" , "P" , "G"]:
            idx = 0
            count = 0
            
            for gar in range(len(garbage)):
                if j in garbage[gar]:
                    count += garbage[gar].count(j)
                    idx  = gar
            result += count + time[idx] 
        return result
        
        
        
#                     brute force
#         count_glass, count_paper,count_metal = 0 , 0 ,0
       
       
#         paper_idx , metal_idx , glass_idx =-1 , -1 ,-1 
        
       
#         for i in range(len(garbage)):
#             if "G" in garbage[i]:
#                 glass_idx = i
#                 count_glass += garbage[i].count("G")
#             if "P" in garbage[i]:
#                 paper_idx = i
#                 count_paper += garbage[i].count("P")
#             if "M" in garbage[i]:
#                 metal_idx = i
#                 count_metal += garbage[i].count("M")
#         time = []
#         time.append(0)
#         for j in range(len(travel)):
#             time.append(time[-1] + travel[j])
#         result = 0
#         result += (time[paper_idx] if paper_idx != -1 else 0) +(time[glass_idx] if             glass_idx != -1 else 0)+(time[metal_idx] if metal_idx != -1 else 0) 
#         result += count_metal + count_paper + count_glass
#         return result


 
        