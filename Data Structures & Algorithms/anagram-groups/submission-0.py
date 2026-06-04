from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_anagrams = defaultdict(list)
        for s in strs:
            # work with individual string
            cnt_array = [0]*26
            for i in s:
                idx = ord(i)-ord('a')
                cnt_array[idx] += 1
            grp_anagrams[tuple(cnt_array)].append(s)
        return list(grp_anagrams.values())