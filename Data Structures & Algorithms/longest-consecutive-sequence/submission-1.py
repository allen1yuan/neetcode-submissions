class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        nums = sorted(set(nums))
        count, res = 1, 1
        pointer = 0
        while pointer < len(nums) - 1:
            if nums[pointer] == nums[pointer + 1] - 1:
                count += 1
            else:
                count = 1
            res = max(count, res)
            pointer += 1
        return res