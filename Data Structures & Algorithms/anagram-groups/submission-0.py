class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            sortS = ''.join(sorted(s))

            if sortS not in groups:
                groups[sortS] = []
            groups[sortS].append(s)

        return list(groups.values())