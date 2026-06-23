class Solution:
    def trap(self, height: List[int]) -> int:
        i,j = 0, len(height)-1
        water = 0
        while i<j:
            if height[i]<height[j]:
                p=i+1
                while height[p]<height[i] and p<len(height):
                    water+=height[i]-height[p]
                    p+=1
                i=p
            else:
                p=j-1
                while height[p]<height[j] and p>0:
                    water+=height[j]-height[p]
                    p-=1
                j=p
        return water
            