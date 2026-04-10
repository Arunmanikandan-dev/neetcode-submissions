class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dis={}
        dia={}
        if len(s)==len(t):
            if set(s)==set(t):
                for i in range(len(s)):
                    if s[i] not in dis:
                        dis[s[i]]=1
                    else:
                        dis[s[i]]+=1
                    if t[i] not in dia:
                        dia[t[i]]=1
                    else:
                        dia[t[i]]+=1
        if dis==dia and len(dis) > 0 or s == t == "":
            return True
        return False             