class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(int) 
        for value , weight in items1 + items2:
            dic[value] += weight
        return sorted(dic.items())
        # merged = defaultdict(int)
        # for value, weight in items1 + items2:
        #     merged[value] += weight
        # return sorted(merged.items())
        

        
        # items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5] , [7,8]]
#         ans=[]           
#         for i in items1:
#             for j in items2:
#                 if i[0] == j[0]:
#                     ans.append([i[0] , i[1] + j[1]])
#                     len(items2) -=1
#                     break
#                 if i[0] != j[0] and items2.index(j)==len(items2)-1:
#                     ans.append([i[0] , i[1]])
#                 if i[0] != j[0] and items1.index(i)==len(items1)-1:
#                     ans.append([j[0] , j[1]])
                    
#         return ans
        
                    