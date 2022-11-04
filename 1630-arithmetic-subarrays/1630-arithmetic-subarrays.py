class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        d = {}
        ans = []
        
        for i in range(len(l)):
            d[i] = nums[l[i]:r[i]+1]
        for ele in d:
            j = 0
            d[ele].sort()
            for i in range(2,len(d[ele])):
                if d[ele][i]-d[ele][i-1]!=d[ele][1]-d[ele][0]:
                    ans.append(False)
                    break
                j+=1
            if j==len(d[ele])-2:
                ans.append(True)
        return ans
        