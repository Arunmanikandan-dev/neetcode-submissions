class Solution:
    def maxArea(self, heights: List[int]) -> int:
        le =len(heights)
        left = 0 
        right =le-1
        maxa =0
        while left <right:
            maxa=max(min(heights[left],heights[right])*(right-left),maxa)
            if heights[left] > heights[right]:
                right-=1
            else:
                left +=1
        return maxa
