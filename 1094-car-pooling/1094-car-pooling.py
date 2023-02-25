class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pref = [0]*1001
        for nums , fro , to in trips:
            
            pref[fro] += nums
            pref[to] -= nums
        
        summ = 0
        for i in range(len(pref)):
            summ += pref[i]
            if summ > capacity:
                return False
        return True
            
        
        
        
        
        
        
        
        
        
        
        
        
        