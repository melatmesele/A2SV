class Solution:
    def longestPalindrome(self, s: str) -> str:
        result, resultLen = "",0
        for i in range(len(s)):
            result, resultLen = computePalindrome(i,i, s, result, resultLen)
            result, resultLen = computePalindrome(i,i+1, s, result, resultLen)
        return result


def computePalindrome(left, right, string, result, resultLen): 
    while left >= 0 and right < len(string) and string[left] == string[right]:
        if (right - left + 1) > resultLen:
            result = string[left:right+1]
            resultLen = right - left + 1
        left -= 1
        right += 1
    return [result, resultLen]
        