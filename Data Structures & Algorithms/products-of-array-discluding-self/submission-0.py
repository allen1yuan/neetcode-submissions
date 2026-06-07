class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]
        for index, n in enumerate(nums):
            for i in range(0, len(nums)):
                if i != index:
                    res[i] *= n
        return res