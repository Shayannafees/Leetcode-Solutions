from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum_value = 0
        for i in range(len(nums)-k + 1):
            total = sum(nums[i:i+k])
            average = total / k
            # print(total)
            if average > maximum_value:
                maximum_value = average
        
        print(maximum_value)
        return maximum_value
    


a = Solution()

arr = [1,12,-5,-6,50,3]

a.findMaxAverage(arr, 4) # type: ignore

#find average of it