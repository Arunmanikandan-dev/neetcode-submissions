class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxx = [0] * n

        # build suffix max array
        maxx[-1] = prices[-1]
        for i in range(n - 2, -1, -1):
            maxx[i] = max(prices[i], maxx[i + 1])

        prom = 0
        for i in range(n - 1):
            prom = max(prom, maxx[i + 1] - prices[i])

        return prom