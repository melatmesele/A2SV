class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = i = 0                            
        m = 0                               
        bs = [-1,-1]                        
        
        for r in range(len(fruits)):             
            if fruits[r]!= bs[1]:               
                if fruits[r] != bs[0]: l = i     
                i = r                        
                bs[0], bs[1] = bs[1], fruits[r]
            m = max(m, r - l + 1)           

        return m
        