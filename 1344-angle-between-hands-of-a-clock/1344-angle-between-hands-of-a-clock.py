class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        bigHand = minutes * 360/60      # minutes hand
        smallHand = 360/12 * (hour%12) + 30/60*minutes      # hours hand
        diff = abs(bigHand - smallHand)

        return min(diff, 360 - diff)    # smaller b/w both

        