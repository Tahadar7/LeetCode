class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = prices.copy()  
        stack = []

        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:

                j = stack.pop()   # index of the item from top of stack
                res[j] = res[j] - prices[i]    # subtract curr price from item
            stack.append(i)         # append curr item in stack

        return res
        