from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lp = len(s1)
        kp = len(s2)

        if lp > kp:
            return False

        dp = Counter(s1)
        window = Counter(s2[:lp])

        if dp == window:
            return True

        for i in range(lp, kp):
            window[s2[i]] += 1
            window[s2[i - lp]] -= 1

            if window[s2[i - lp]] == 0:
                del window[s2[i - lp]]

            if window == dp:
                return True

        return False