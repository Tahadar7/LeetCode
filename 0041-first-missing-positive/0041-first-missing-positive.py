class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)

        num = 1
        while num in num_set:       # if number is present in set
            num += 1

        return num      # num not in set
        