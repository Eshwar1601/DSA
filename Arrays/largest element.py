#largest element
class Solution:
    def largest(self, arr):
        # code here
        max=arr[0]
        for i in range(1,len(arr)):
            if arr[i]>max:
                max=arr[i]
        return max
