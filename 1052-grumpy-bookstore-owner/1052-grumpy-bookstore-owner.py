class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        summ = 0
        
        counter = 0
        ans = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                summ += customers[i]
        left = 0
        for i in range(len(grumpy)):
            if i < minutes:
                
                if grumpy[i]== 1:
                    summ += customers[i]
            else:
                if grumpy[i]== 1:
                    summ += customers[i]
                if grumpy[left]== 1:
                    summ -= customers[left]
                left += 1
            ans = max(summ , ans)
        return ans
            
                
                
        