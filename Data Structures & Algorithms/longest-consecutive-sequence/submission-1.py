class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        maxlen = 1
        r = 1
        if len(nums)==0:
            return 0
        length = 1
        while r<len(nums):
            if nums[r]==nums[r-1]:
                pass
            elif nums[r]==nums[r-1]+1:
                length += 1
            else:
                maxlen = max(length, maxlen)
                length = 1   
            r += 1
        return max(maxlen, length)
                      