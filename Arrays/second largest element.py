#second largest
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        f_largest=s_largest=-1
        for i in arr:
            if i>f_largest:
                s_largest=f_largest
                f_largest=i
            elif i>s_largest and i!=f_largest:
                s_largest=i
        return s_largest

