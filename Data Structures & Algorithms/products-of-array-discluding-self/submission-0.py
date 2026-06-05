class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]
        post = [1]
        for i in range(1,n):
            pre.append(pre[i-1]*nums[i-1])
            post.append(post[i-1]*nums[n-i])
        product_array = [pre[i]*post[n-1-i] for i in range(n)]
        return product_array
