from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1 = Counter(s)
        w2 = Counter(t)
        return w1 == w2      
        