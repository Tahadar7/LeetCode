class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        if not nums:
            return False
        mid = (len(nums) - 1)//2

        for i in range(len(nums)):
            if (i != mid and nums[i] == nums[mid]):
                return False

        return True
        