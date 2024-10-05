from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dick = {}
        for index, val in enumerate(nums):
            difference = target - val
            if difference in dick:
                return [dick[difference], index]
            dick[val] = index
