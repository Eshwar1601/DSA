#sorted and rotated or not
class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        count=0
        for i in range(len(nums)):
            if nums[i]>nums[(i+1)%len(nums)]:
                count+=1
        return count<=1