class TimeMap:

    def __init__(self):
        self.st = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.st:
            self.st[key] = {}

        self.st[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.st:
            return ""

        k = self.st[key].get(timestamp, None)

        if k is not None:
            return k

        ty = list(self.st[key].keys())
        ty.sort()

        l = 0
        r = len(ty) - 1

        res = -1

        while l <= r:

            mid = (l + r) // 2

            if ty[mid] <= timestamp:
                res = ty[mid]
                l = mid + 1
            else:
                r = mid - 1

        if res == -1:
            return ""

        return self.st[key][res]