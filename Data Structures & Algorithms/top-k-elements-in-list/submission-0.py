from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        wc = Counter(nums)
        k_common = wc.most_common(k)
        elems = [a for a,b in k_common]
        return elems