from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: # type: ignore
        a = sorted(nums)            #[2,3,4,4,5,10,20]
        curr_streak = 1
        longest = curr_streak
        i,j = 0,1

        if not nums:
            return 0
        
        while i < len(nums) and j < len(nums):
            if a[i] + 1 == a[j]:
                curr_streak += 1
                longest = max(longest, curr_streak)
                i+= 1
                j+= 1
            elif a[i] == a[j]:
                i += 1
                j += 1
            else:
                curr_streak = 1
                i += 1
                j += 1

        return max(longest, curr_streak)



s = Solution()
print(s.longestConsecutive([0,3,2,5,4,6,1,1]))