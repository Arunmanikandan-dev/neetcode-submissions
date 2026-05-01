class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ct = 0
        t = ""
        
        for i in s:
            if i not in t:
                t += i
            else:
                p = t.index(i)
                ct = max(ct, len(t))
                t = t[p+1:]  # remove duplicate and everything before
                t += i       # add current char
        
        ct = max(ct, len(t))
        return ct