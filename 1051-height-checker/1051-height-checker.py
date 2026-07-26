class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)      # new arr for comparison

        return sum(h!= e for h, e in zip(heights, expected))
        