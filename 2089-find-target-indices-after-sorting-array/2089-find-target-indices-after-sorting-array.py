class Solution:
    def targetIndices(self, nums, target):
        lt_count = eq_count = 0
        for n in nums:
            if n < target:
                lt_count += 1
            elif n == target:
                eq_count += 1
            
        return list(range(lt_count, lt_count+eq_count))