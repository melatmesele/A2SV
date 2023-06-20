class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = ""
        summ = 0
        answer =[]
        for i in digits:
            result += str(i)
        summ = str(int(result) + 1)
        for j in summ:
            answer.append(int(j))
        return answer