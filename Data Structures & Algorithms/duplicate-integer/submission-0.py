class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dit = {}
        for i in nums:
            if i in dit:
                return True
            dit[i]=1
        return False