class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        result = []
        dictionary = {value: index  for index , value in enumerate(s)}
        
        start = 0
        end = 0 
        for index2 , value2 in enumerate(s):
            end = max(end , dictionary[value2])
            if index2 == end:
                result.append(end - start + 1)
                start = end + 1
        return result
        
