class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a=[]
        for x in range(0, len(nums)-1):
            for y in range(x+1, len(nums)):
                if nums[x]+nums[y]==target:
                    a = [x, y]
        return a      
        