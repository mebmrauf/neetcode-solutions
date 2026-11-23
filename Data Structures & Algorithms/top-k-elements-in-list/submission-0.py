class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        sorted_dict = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))

        out = []
        for key, val in sorted_dict.items():
            if len(out) == k:
                break
            out.append(key)

        return out