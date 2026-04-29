class Solution:

    def encode(self, strs: List[str]) -> str:
        k = ""
        for i in strs:
            k += str(len(i)) + "#" + i    
        return k

    def decode(self, s: str) -> List[str]:
        strs = []
        kp = 0

        while kp < len(s):
            j = kp

            # find '#'
            while s[j] != "#":
                j += 1

            # get length
            m = int(s[kp:j])

            # extract string
            word = s[j+1 : j+1+m]
            strs.append(word)

            # move pointer
            kp = j + 1 + m

        return strs