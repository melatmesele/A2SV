class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = 0
        result = []
        diff = []
        while right < k:
            result.append(arr[right])
            diff.append(abs(arr[right] - x))
            right += 1
        while right < len(arr):
            difference = abs(arr[right] - x)
            if difference < diff[left] or  result[0] == arr[right]:
                diff.append(difference)
                result.remove(result[0])
                result.append(arr[right])
                left += 1
            # elif difference == diff[left] and result[0] > arr[right]:
                
            else:
                break
            right += 1
        return result
            
        