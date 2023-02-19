class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dic = defaultdict(int)
        counter = 0
        left = 0
        
        for i in range(len(s)):
            
            dic[s[i]] += 1
            
            while len(dic) == 3:
                counter += len(s) - i
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    del dic[s[left]]
                left += 1
        return counter
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
#         dic1 = {"a":1 , "b":1  , "c":1}
        
#         counter = 0
#         for i in range(len(s)-2):
#             dic2 = {}
#             for j in range(i , len(s)):
#                 dic2[s[j]]= 1
#                 if dic1 == dic2:
#                     counter +=1
#         return counter
        
        
        
        
        
        
#     seen = {"a":0,"b":0,"c":0}
# 	i = j = 0
# 	count = 0
# 	n = len(s)
# 	while i + 3 <= n:
# 		if seen["a"] >=1 and seen["b"] >=1 and seen["c"] >=1:
# 			seen[s[i]] -=1
# 			i +=1
# 			count += n-j+1
# 		else:
# 			if j <= n-1:
# 				seen[s[j]] +=1
# 				j +=1
# 			else:
# 				break
# 	return count