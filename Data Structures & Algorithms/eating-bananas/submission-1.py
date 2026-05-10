def check(piles, h, k):
    result = 0
    for i in piles:
        result += (i+k-1)//k
    return result <= h


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = (sum(piles)+h-1)//h
        right = max(piles)

        ans = right

        while left <= right:

            mid = (left + right) // 2

            if check(piles, h, mid):

                ans = mid
                right = mid - 1

            else:
                left = mid + 1

        return ans