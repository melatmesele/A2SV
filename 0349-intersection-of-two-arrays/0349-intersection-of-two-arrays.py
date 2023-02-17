class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
         
        sett ,  result = set() , []
        nums1p,nums2p = 0 ,0
        nums2.sort()
        nums1.sort()
        # temp = [[0]*4]*4
        # temp[0][0] = 1
        # print (temp)
        while(nums1p  < len(nums1) and nums2p < len(nums2)):
            if nums1[nums1p ] < nums2[nums2p]:
                nums1p  += 1
            elif nums1[nums1p ] > nums2[nums2p]:
                nums2p += 1
            else:
                sett.add(nums1[nums1p ])
                nums1p += 1
                nums2p += 1
        for item in sett:
            result.append(item)
        return result
                
            
        
        
        
        
        
        
        
#         
            
            
            
            
            
#         brute force
        # result = []
        # sett = set()
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             sett.add(nums1[i])
        # for k in sett:
        #     result.append(k)
        # return result
        