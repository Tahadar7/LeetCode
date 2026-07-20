class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        freq = [0] * 24
        res = 0
        for hour in hours:
            rem = hour % 24
            target = (24 - rem) % 24        # check for target rem
            res += freq[target]         # add in res if target exists

            freq[rem] += 1              # for future target checks
        return res       