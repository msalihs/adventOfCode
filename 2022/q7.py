from pathlib import PurePath
from collections import defaultdict


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        readings = f.read().split("\n")
        fs = defaultdict(list)
        curr = PurePath("/")
        for reading in readings:
            if reading[:4] == "$ cd":
                if reading[5:7] == "..":
                    curr = curr.parent
                else:
                    curr = curr / reading[5:]
            elif reading[:4] not in {"dir ", "$ ls"}:
                size, name = reading.split(" ")
                size = int(size)
                fs[curr].append((name, size))

        sizes = dict()
        for p in fs:
            _sum = 0
            for name, size in fs[p]:
                _sum += size
            while p != PurePath("/"):
                sizes[p] = sizes.get(p, 0) + _sum
                p = p.parent
            sizes[p] = sizes.get(p, 0) + _sum

        _max = 70000000
        required = 30000000
        needed = required - _max + sizes[PurePath("/")]
        result2 = sizes[PurePath("/")]
        for p in sizes:
            if sizes[p] < 100000:
                result1 += sizes[p]
            if result2 > sizes[p] > needed:
                result2 = sizes[p]

        return result1, result2


solver = Solution()
print(solver.solve("/home/msafa/adventOfCode/2022/q7.txt"))
