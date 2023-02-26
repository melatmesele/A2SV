class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        pref = [0]*len(arr)
        pref[0] = arr[0]
        
        for item in range(1, len(arr)):
            pref[item] = pref[item -1] + arr[item]
        summ = 0
        
        for i in range(len(pref)):
            end = i
            
            while end < len((pref)):
                if i== 0:
                    summ += pref[end]
                else:
                    value = pref[end] - pref[i-1]
                    summ += value
                end += 2
        return summ
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         answer = 0
#         n = len(arr)
#         for i in range(n):
#             summation = 0
#             for j in range(i , n):
#                 summation += arr[j]
#                 if (i + j) % 2 == 0:
#                     answer += summation
#         return answer 
                
