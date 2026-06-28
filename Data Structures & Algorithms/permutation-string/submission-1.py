class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # abc lecabee
        def pos_abc(v):
            return ord(v) - ord('a')

        # get the word count
        wc = [0]*26
        for i in s1:
            wc[pos_abc(i)] += 1

        # [1 1 1 0 0 0 0 0]
        for i in range(len(s2)+1-len(s1)):
            print(f"{i=}")
            wc2 = wc.copy()
            for j in range(i,i+len(s1)):
                print(f"{j=}")
                if wc2[pos_abc(s2[j])] > 0:
                    wc2[pos_abc(s2[j])] -= 1
                    if sum(wc2)==0:
                        return True
                else:
                    break
        return False
