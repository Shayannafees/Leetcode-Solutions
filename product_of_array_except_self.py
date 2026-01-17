from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: # type: ignore
        n = len(nums)
        output = [1] * n            # [1,1,1,1]
        prefix = 1
        for i in range(n): 
            output[i] = prefix                      #1 = 1
            prefix = prefix * nums[i]               #prefix = 1 * 1


        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] = output[i] * suffix
            suffix = suffix * nums[i]

        return output


s = Solution()
print(s.productExceptSelf([1,2,4,6]))
# print(s.productExceptSelf([0,-6,0,0,0]))

