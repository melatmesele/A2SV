class Solution:
    def frequencySort(self, s: str) -> str:
        # dic = defaultdict(int)
        # for i in s:
        #     dic[i] += 1
        dic = Counter(s)
        s = list(set(s))
        s.sort(key= lambda x: dic[x] * -1)
        output = [x * dic[x] for x in s]
        return "".join(output)
#         ans = []
#         for item in dic:
#             ans.append((-(dic[item]) , item))
#         ans.sort()
#         result = ''
#         for i in ans:
            
#             result += i[1]* -(i[0])
        # return result
                
        
            
        