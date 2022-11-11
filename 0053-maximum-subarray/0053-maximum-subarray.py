class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
#          -2  1  -3  4 -1  2  1  -5  4
#                     i                                                  
#                                                             max = -2
#                                     j                                              
                                                #          step1
                                                # total = 4      total = p2 = 1   total = -2
                                                # total =      p1 = 1           p=1
                                                # p2 =  4      p2 = 2           p2 = 3
                                                # largest = 6    largest 1        largest = 1
                    largest = -math.inf
                    total = 0
                    i = 0
                    j = 0
                    while(j < len(nums)):
                        if total >= 0:
                            total += nums[j]
                            j += 1
                            largest= max(total , largest)
                        else:
                            i = j
                            total = nums[j]
                            j += 1
                            largest = max(total , largest)
                    return largest
                            
                                                           
                                                                
            
                                                            
#         p1, p2 = 0, 0
#         largest = -math.inf
#         total = 0
#         while p2 < len(nums):
#             if total >= 0:                
#                 total += nums[p2]
#                 p2 += 1
#                 largest = max(largest, total)
#             else:
#                 p1 = p2                
#                 total = nums[p2]
#                 largest = max(largest, total)
#                 p2 +=1
#         return largest 