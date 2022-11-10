class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        d = {c:i for i, c in enumerate(s)}

        l = 0
        r = 0
        ans = []
        for i, c in enumerate(s):  
            r = max(r, d[c])
            if i == r:
                ans += [r - l + 1]
                l = r + 1

        return ans
        