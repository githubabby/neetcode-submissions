from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,k
        maxR=min(len(s),k+1) 
        while r<len(s):
            val,freq = Counter(s[l:r+1]).most_common(1)[0]
            rr = k- (len(s[l:r+1])-freq)
            if rr>=0:
                maxR = max(maxR, len(s[l:r+1]))
                r+=1
            else:
                l+=1
        return maxR

            