class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        dic = defaultdict(int)
        counter = 0
        left = 0
        if len(s) < 3:
            return 0
        for i in range(3):
            dic[s[i]] += 1
        if len(dic) == 3:
            counter += 1
        
        for i in range(3 , len(s)):
            
            
            dic[s[i]] += 1
            dic[s[left]] -= 1
            
            if dic[s[left]] == 0:
                del dic[s[left]]
            
            if len(dic) == 3:
                counter += 1
            left += 1
        return counter
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         counter = 0
#         left = 0
#         right = 2
#         d = defaultdict(int)
        
#         for i in range(0 , min(len(s), 2)):
#             d[s[i]] += 1
        
#         while right < len(s):
#             d[s[right]] +=1
#             if len(d) == 3:
#                 counter +=1
#             d[s[left]]-=1
#             if d[s[left]] == 0:
#                 del(d[s[left]])
#             right +=1 
#             left += 1
#         return counter
            
            
            
#         counter = 0 
#         left = 0
#         right = 2
        
#         while(right < len(s)):
#             dicti = {}
#             for i in range(left , right+1):
                
#                 dicti[s[i]] = 1
#             if len(dicti) == 3:
#                 counter +=1
            
#             left +=1
#             right += 1
#         return counter
          
          
          
        