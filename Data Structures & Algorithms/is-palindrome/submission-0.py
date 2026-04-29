class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if str ==str[::-1]:
        #   return True
        # return Flase
        s= ''.join(ch.lower() for ch in s if ch.isalnum())
        #print(s)
        c=len(s)
        k=c//2
        for i in range(k):
            if s[i]!=s[c-i-1]:
                return False
        return True