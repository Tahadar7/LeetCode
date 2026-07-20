class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:       # tar > last element
            return len(nums)
        if target < nums[0]:        # tar < first element
            return 0

        l = 0
        r = len(nums) - 1

        while l<=r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m+ 1
            else:
                r = m - 1   
        return l    
        