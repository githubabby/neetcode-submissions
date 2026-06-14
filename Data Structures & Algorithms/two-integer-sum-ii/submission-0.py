class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # case 1 - value equal target - return l+1, r+1
        # case 2 - value is less than target - left move ahead
        # case 3 - value is more than target - right moves back
        # while l<r

        l = 0
        r = len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l]+numbers[r] < target:
                l += 1
            else:
                r -= 1