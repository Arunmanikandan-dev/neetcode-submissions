class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) >= 2:
            nums = sorted(nums)
            count = 1
            max_count = 1
            prev = nums[0]

            for i in nums[1:]:
                if i == prev:
                    continue   # skip duplicates
                elif prev + 1 == i:
                    count += 1
                else:
                    count = 1  # reset
                
                max_count = max(max_count, count)
                prev = i

            return max_count

        elif len(nums) == 1:
            return 1
        else:
            return 0