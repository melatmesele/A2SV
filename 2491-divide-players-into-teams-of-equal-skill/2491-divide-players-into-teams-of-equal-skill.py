class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill =sorted(skill)
        left = 0
        right = len(skill) - 1
        summ = skill[left] + skill[right]
        result = 0
        while(left <= right):
            if skill[left] + skill[right] != summ:
                return -1
            else:
                result += (skill[left]*skill[right])
                left += 1
                right -= 1
                
        return result
                