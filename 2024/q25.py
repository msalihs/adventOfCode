import time
from enum import Enum


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        schematics = f.read().split("\n\n")
        keys = list()
        locks = list()

        for schematic in schematics:
            grid = [line.strip() for line in schematic.split("\n")]
            n, m = len(grid), len(grid[0])
            result = [0] * m
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == "#":
                        result[j] += 1
            if grid[-1][-1] == "#":
                locks.append([x - 1 for x in result])
            else:
                keys.append([x - 1 for x in result])

        # PART 1
        for key in keys:
            for lock in locks:
                for x, y in zip(key, lock):
                    if x + y + 1 >= n:
                        break
                else:
                    result1 += 1

        return result1, result2


start = time.time()
solver = Solution()
print(solver.solve("2024/q25.txt"))
print(f"Time: {time.time() - start}")
