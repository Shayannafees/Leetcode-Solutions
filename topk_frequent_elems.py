from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for i in nums:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1

        top_keys = sorted(hm, key=hm.get, reverse=True)[:k] # type: ignore
        return top_keys
    

s = Solution()
print(s.topKFrequent([1,2,2,3,3,3], k = 2))

