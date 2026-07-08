class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low = 1
        high = max(nums)

        while (low < high):
            m = low + (high - low)// 2

            operations = 0
            for num in nums:
                operations += (num - 1) // m
            
            if operations <= maxOperations:
                high = m
            else:
                low = m + 1
        return low

            

        