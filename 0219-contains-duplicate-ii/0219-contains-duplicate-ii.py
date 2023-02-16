class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        dic ={}
        flag = False
        for right in range(len(nums)):
            if right - left > k:
                del dic[nums[left]]
                left += 1
            if nums[right] in dic:
                return True
            else:
                dic[nums[right]] = 1
        return flag
#         dic = {}
#         left = 0
#         right = 0
#         if len(nums) == 1:
#             return False
#         while right <= k and right < len(nums):
#             if nums[right] in dic:
#                 return True
#             dic[nums[right]] =1
#             right += 1
# #         if len(dic)== k:
# #             return True
          
#         flag = False
#         while right < len(nums):
#             del dic[nums[left]]
#             if nums[right] in dic:
#                 return True
#             else:
            
#                 dic[nums[right]] = 1
#             left += 1
#             right += 1
#         return flag
                