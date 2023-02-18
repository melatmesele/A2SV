class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        counter = 0
        result = float('INF')
        n = len(blocks)
        for right in range(n):

            if right - left +1  <= k:
                if blocks[right] == "W":
                    counter += 1
           
                
            else:  
                if blocks[right]=="W":
                    counter += 1
                if blocks[left] == "W":
                    counter -= 1
                left += 1
            if right - left +1  == k:
                result = min(result , counter)
                

            if left > n-k:
                break
        return result
        #brute force
#         n = len(blocks)
#         result = float('INF')
#         for i in range(n-k+1):
#             counter = 0
#             occu = 1
#             if blocks[i] == "W":
#                 counter = 1
#             for j in range(i+1 , n):
#                 occu += 1
#                 if blocks[j] == "W":
#                     counter += 1
                
#                 if occu == k:
#                     break
#             result = min(result , counter)
#         return result