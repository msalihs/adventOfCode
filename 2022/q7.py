from pathlib import Path
from collections import defaultdict


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        readings = f.read().split("\n")
        fs = defaultdict(list)
        curr = Path("/")
        for reading in readings:
            if reading[:4] == "$ cd":
                if reading[5:7] == "..":
                    curr = curr.parent
                else:
                    curr = curr / reading[5:]
            elif reading[:4] == "$ ls":
                continue
            elif reading[:3] != "dir":
                size, name = reading.split(" ")
                size = int(size)
                fs[curr].append((name, size))

        sizes = dict()
        for p in fs:
            _sum = 0
            for name, size in fs[p]:
                _sum += size
            while p != Path("\\"):
                sizes[p] = sizes.get(p, 0) + _sum
                p = p.parent
            sizes[p] = sizes.get(p, 0) + _sum

        _max = 70000000
        required = 30000000
        needed = required - _max + sizes[Path("\\")]
        result2 = sizes[Path("\\")]
        for p in sizes:
            if sizes[p] < 100000:
                result1 += sizes[p]
            if result2 > sizes[p] > needed:
                result2 = sizes[p]

        return result1, result2


solver = Solution()
print(solver.solve("2022/q7.txt"))
