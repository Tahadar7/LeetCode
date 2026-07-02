class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index_start = 0
        for i in range(len(nums)):
            if nums[i] != 0:     # move non zero to start of the lsit
                nums[index_start] = nums[i]
                index_start += 1

        # assign zero to remaining list with slicing
        nums[index_start:] = [0] * (len(nums) - index_start)
        