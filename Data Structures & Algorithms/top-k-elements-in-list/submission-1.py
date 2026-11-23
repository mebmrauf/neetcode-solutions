class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        sorted_nums = sorted(count, key=lambda x: count[x], reverse=True)

        return sorted_nums[:k]