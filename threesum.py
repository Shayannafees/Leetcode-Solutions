from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: # type: ignore
        #[-1,-1,0,1,2,4]
        nums.sort()
        print(nums)
        
        arra = []

        for a in range(len(nums)-2):        #it should be what?
            #do i check nums[a] != nums[a-1] here?
            if a > 0 and nums[a] == nums[a-1]:
                continue
            i = a + 1   
            j = len(nums) - 1
            while i < j:        
                total = nums[a] + nums[i] + nums[j]
                if total == 0:          
                    arra.append([ nums[a], nums[i], nums[j]])
    
                    i += 1      
                    j -= 1
                    #skip duplicates for i
                    while i<j and nums[i] == nums[i-1]:
                        i+=1
                    #skip duplicates for j
                    while i<j and nums[j] == nums[j+1]:
                        j -= 1

                elif total > 0:
                    j -= 1
                else:
                    i += 1

        return arra



s = Solution()
print(s.threeSum([0,0,0]))
print(s.threeSum([-1,0,1,2,-1,-4]))