from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0, len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] == target and i < j:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                i += 1
                j -= 1
        return []
    


s = Solution()
print(s.twoSum([1,2,3,4], 3))
print(s.twoSum([-5,-3,0,2,4,6,8], 5))

