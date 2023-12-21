import csv
import numpy


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        grid = [list(row) for row in f.read().split("\n") if row]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "S":
                    start = (i, j)

        turns = 64
        plots = {start}
        for _ in range(turns):
            next_plots = set()
            while plots:
                i, j = plots.pop()
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]):
                        if grid[i + di][j + dj] in {".", "S"}:
                            next_plots.add((i + di, j + dj))
            plots = next_plots.copy()

        result1 = len(plots)
        turns = 400
        plots = {start}
        y = list()
        x = list()
        for idx in range(turns):
            next_plots = set()
            while plots:
                i, j = plots.pop()
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if grid[(i + di) % (len(grid))][(j + dj) % (len(grid[0]))] in {
                        ".",
                        "S",
                    }:
                        next_plots.add((i + di, j + dj))
            plots = next_plots.copy()
            y.append(len(plots))
            x.append(idx + 1)

        target = 26501365
        res = target % len(grid)
        indices = [i * len(grid) + res - 1 for i in range(3)]
        a, b, c = numpy.polyfit([x[i] for i in indices], [y[i] for i in indices], 2)
        result2 = round(a * (target ** 2) + b * target + c)

        return result1, result2


solver = Solution()
print(solver.solve("2023/q21.txt"))
