from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dit = defaultdict(list)

        for k in strs:
            count = [0] * 26
            for l in k:
                count[ord(l) - ord("a")] += 1
            dit[tuple(count)].append(k)

        return list(dit.values())