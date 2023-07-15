#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        minim = arr[0]
        left = 0
        right = 1
        
        if n == 1:
            return 1
        while(right <= n-1):
            if arr[left] > arr[right]:
                return 0
            else:
                if minim > arr[left]:
                    return 0
            right += 1
            left += 1
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.arraySortedOrNot(arr, n)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1

# } Driver Code Ends