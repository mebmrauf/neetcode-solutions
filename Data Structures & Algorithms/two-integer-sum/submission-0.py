class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for i, num in enumerate(nums):
            searching = target - num

            if searching in found:
                return [found[searching], i]

            found[num] = i