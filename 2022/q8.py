from pathlib import Path
from collections import defaultdict


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = set(), 0
        readings = f.read().split("\n")
        grid = []

        print(grid)
        for reading in readings:
            grid.append([int(c) for c in reading])

        # scan from left
        for i in range(len(grid)):
            j = 0
            curr = grid[i][j]
            result1.add((i, j))
            j += 1
            while j < len(grid[0]) and curr < 9:
                if grid[i][j] > curr:
                    result1.add((i, j))
                    curr = grid[i][j]
                j += 1

        # scan from right
        for i in range(len(grid)):
            j = len(grid[0]) - 1
            curr = grid[i][j]
            result1.add((i, j))
            j -= 1
            while j >= 0 and curr < 9:
                if grid[i][j] > curr:
                    result1.add((i, j))
                    curr = grid[i][j]
                j -= 1

        # scan from top
        for j in range(len(grid[0])):
            i = 0
            curr = grid[i][j]
            result1.add((i, j))
            i += 1
            while i < len(grid) and curr < 9:
                if grid[i][j] > curr:
                    result1.add((i, j))
                    curr = grid[i][j]
                i += 1

        # scan from bottom
        for j in range(len(grid[0])):
            i = len(grid) - 1
            curr = grid[i][j]
            result1.add((i, j))
            i -= 1
            while i >= 0 and curr < 9:
                if grid[i][j] > curr:
                    result1.add((i, j))
                    curr = grid[i][j]
                i -= 1

        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                score = 1
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    k, l = i, j
                    curr = grid[k][l]
                    trees = 0
                    while 0 <= k + di < len(grid) and 0 <= l + dj < len(grid[0]):
                        k, l = k + di, l + dj
                        trees += 1
                        if grid[k][l] >= curr:
                            break
                    if trees == 0:
                        break
                    score *= trees
                result2 = max(result2, score)

        return len(result1), result2


solver = Solution()
print(solver.solve("2022/q8.txt"))
