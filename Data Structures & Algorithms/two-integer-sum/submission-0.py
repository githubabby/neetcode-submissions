class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        if nums:
            hashmap[nums[0]] = 0
        for i in range(1, len(nums)):
            comp = target - nums[i]
            if comp in hashmap.keys():
                return [hashmap[comp], i]
            else:
                hashmap[nums[i]] = i
        return False