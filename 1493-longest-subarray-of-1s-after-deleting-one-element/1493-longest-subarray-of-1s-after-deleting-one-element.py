class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        counter = 0
        maxim = 0
        dic = collections.defaultdict(int)
        if 0 not in nums:
            return len(nums) -1
        else:
            for right in range(len(nums)):
                dic[nums[right]] += 1
                if nums[right] == 1:
                    counter += 1
                while dic[0] == 2:
                    if nums[left] == 1:
                        counter -= 1
                    dic[nums[left]] -= 1

                    left += 1
                maxim = max(maxim , counter)
        return maxim
#         brute force
#         maxim = 0
#         if 0 not in nums:
            
#             return len(nums) - 1
#         else:    
#             for i in range(len(nums)-1):
#                 dic = collections.defaultdict(int)
#                 dic[nums[i]] = 1
                
#                 counter = 0
#                 if nums[i] == 1: 
#                         counter = 1
                
#                 for j in range(i+ 1 , len(nums)):
#                     if nums[j] == 1: 
#                         counter += 1
#                     dic[nums[j]] +=1
#                     if  dic[0] == 2:
#                         break
#                         # dic[nums[k]] -= 1
#                         # if dic[nums[k]] == 1:
#                         #     counter -= 1
#                         # k +=1
#                     # if dic[nums[j]] == 1: 
#                     #     counter += 1
                    
#                     maxim = max(maxim , counter) 
            
             
        return maxim
        