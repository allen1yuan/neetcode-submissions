class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = []
        for i, h in enumerate(heights):
            for j, hh in enumerate(heights):
                area.append(min(h, hh) * (j-i))
        return max(area)