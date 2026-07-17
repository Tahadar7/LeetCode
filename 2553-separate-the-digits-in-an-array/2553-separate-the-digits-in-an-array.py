class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            res.extend(map(int, str(num)))  # num to str, extend each char as int in list
        return res

        