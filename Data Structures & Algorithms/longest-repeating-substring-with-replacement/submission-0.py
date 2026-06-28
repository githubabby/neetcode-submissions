from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # "AAABBAAABB" 2
        l=0
        r=k
        maxR=min(len(s),k+1) 
        while r<len(s):
            print(l,r,s[l:r+1], maxR)
            val,freq = Counter(s[l:r+1]).most_common(1)[0]
            ru = len(s[l:r+1])-freq
            rr = k-ru
            print(val,freq,ru,rr)
            if rr>=0:
                maxR = max(maxR, len(s[l:r+1]))
                r+=1
            else:
                l+=1
        return maxR

            