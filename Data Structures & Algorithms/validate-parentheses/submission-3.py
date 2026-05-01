from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2:
            return False
        dt={')':'(', '}':'{', ']':'['}
        l=dt.keys()
        m=deque()
        for i in range(len(s)-1,-1,-1):
            print(m,i)
            if s[i] in dt.keys():
                m.append(s[i])
            else:
                if len(m)<1:
                    return False
                k=m.pop()
                print(k,dt[k],s[i])
                if dt[k]!=s[i]:
                    return False
        if len(m)!=0:
            return False
        return True