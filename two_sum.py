from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for ind,val in enumerate(nums):
            print(ind, val)
            s = target - val        # 7-3=4
            if s in hm:
                print(s,ind)
                return [hm[s],ind]
            else:
                hm[val] = ind
        return []


s = Solution()
print(s.twoSum([3,4,5,6], 7))

