class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#            a = [-1 , 0 ,1, 2,-1 , -4]
#             [-4 ,- 1, -1, 0 , 1, 2]
#                           i
#                               l                            ans [[-1,-1,2] , [-1, 0 ,1]]
#                                  r
            nums.sort()
            
            res =[]
            for i in range(len(nums)):
                r = len(nums)-1
                l = i + 1
                while(l < r):
                    if nums[i] + nums[l] + nums[r] > 0:
                        r -=1
                    elif nums[i] + nums[l] + nums[r] < 0:
                        l += 1
                    else: 
                        res.append((nums[i] , nums[l] , nums[r]))
                        r-= 1
                        l += 1
            return set(res)
                        
                        
                
                
                
           