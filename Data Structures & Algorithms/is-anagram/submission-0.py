class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortS, sortT = sorted(s), sorted(t)
        if sortS == sortT: return True
        else: return False