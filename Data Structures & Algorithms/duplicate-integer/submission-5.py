class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        setLength = len(set(nums))
        if length != setLength: return True
        else: return False