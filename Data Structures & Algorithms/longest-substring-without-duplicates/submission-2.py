class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxc = 0
        l,r = 0,0
        wmap = {}
        # abba dvdf abcabcabcb axcfs aaaa aaab bsssa
        while r<len(s):
            v = s[r]
            if v in wmap.keys():
                print(v,'present')
                l=max(l,wmap[v]+1)
                wmap[v]=r
            else:
                print(v,"not present")
                wmap[v]=r
            r+=1
            c=r-l
            maxc = max(maxc,c)
            print(l,r,c, wmap)
        return maxc


        
            