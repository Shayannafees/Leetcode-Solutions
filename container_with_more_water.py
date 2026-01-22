from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int: # type: ignore
        
        i,j = 0, len(heights) - 1
        max_h = 0

        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            max_h = max(max_h, area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_h





    
s = Solution()
print(s.maxArea([1,7,2,5,4,7,3,6]))