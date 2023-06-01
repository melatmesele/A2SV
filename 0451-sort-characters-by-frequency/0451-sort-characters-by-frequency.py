class Solution:
    def frequencySort(self, s: str) -> str:
        # dic = defaultdict(int)
        # for i in s:
        #     dic[i] += 1
        dic = Counter(s)
        ans = []
        for item in dic:
            ans.append((-(dic[item]) , item))
        ans.sort()
        result = ''
        for i in ans:
            
            result += i[1]* -(i[0])
        return result
        
        
            
        