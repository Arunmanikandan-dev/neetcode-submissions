class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        l = ""
        
        for i in range(len(strs[0])):
            t = strs[0][i]
            
            for j in strs[1:]:
                if i >= len(j) or j[i] != t:
                    return l
            
            l += t
        
        return l