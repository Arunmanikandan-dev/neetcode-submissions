class Solution:
    def calPoints(self, operations: List[str]) -> int:
        L = []
        for i in operations:
            if "+"==i:
                L.append(L[-1]+L[-2])
            elif "C"==i:
                L = L[:-1]
            elif "D"==i:
                L.append(2*L[-1])
            else:
                L.append(int(i))
        return sum(L)