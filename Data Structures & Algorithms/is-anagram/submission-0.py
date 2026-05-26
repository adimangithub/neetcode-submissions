from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # Optimization
            return False
        return Counter(s) == Counter(t)