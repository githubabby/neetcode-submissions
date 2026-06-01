class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        wc = {}
        for i in nums:
            if i in wc.keys():
                return True
            else:
                wc[i] = 1
        return False