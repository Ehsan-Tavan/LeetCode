from typing import List


class Solution:
    def containsDuplicate_1(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        return True

    def containsDuplicate_2(self, nums: List[int]) -> bool:
        seen = set()
        for item in nums:
            if item in seen:
                return True
            seen.add(item)
        return False
