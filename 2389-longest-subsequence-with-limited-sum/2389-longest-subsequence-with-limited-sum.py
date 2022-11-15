class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        
        prefixSum = [0]*n
        prefixSum[0] = nums[0]
        res = []
        
        for i in range(1,n):
            prefixSum[i] = nums[i]+prefixSum[i-1]     
        
        for query in queries:
            i, j = 0, n   
            while i<j:
                mid = i+(j-i)//2 
                if prefixSum[mid] > query:
                    j = mid
                else:
                    i = mid+1
            res.append(i)
        return res
#         nums.sort()
#         ll=[]
#         [1,2,4,5]
        
#         for i in range(len(queries)):
#             summ = 0
#             count=0
#             for j in nums:
#                 if j <= queries[i] and summ + j <=queries[i]:
#                     summ+= j
#                     count+=1
#                 else:
#                     break
        
                    
            # queries[i] = count
        #     ll.append(count)
        # return ll
#         nums.sort()
#         for i in range(len(queries)):
#             counter=0
#             summ=0
#             for j in nums:
#                 if j <= queries[i] and summ+j <=queries[i]:
#                     summ+=j
                    
                        
#                     counter+= 1
#                 else:
#                     break
#             queries[i]=counter
#         return queries