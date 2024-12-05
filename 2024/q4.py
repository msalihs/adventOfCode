import itertools


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        grid = [line.strip("\n") for line in f.readlines()]

        n = len(grid)
        m = len(grid[0])

        def check_for_xmas(i, j, di, dj):
            for k in range(4):
                if (
                    i + k * di < 0
                    or i + k * di >= n
                    or j + k * dj < 0
                    or j + k * dj >= m
                ):
                    return False
                if grid[i + k * di][j + k * dj] != "XMAS"[k]:
                    return False
            return True

        # PART 1
        for i in range(n):
            for j in range(m):
                for di, dj in itertools.product([-1, 0, 1], repeat=2):
                    if di == dj == 0:
                        continue
                    if check_for_xmas(i, j, di, dj):
                        result1 += 1

        # PART 2

        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if grid[i][j] == "A":
                    if (
                        (grid[i - 1][j - 1] == "S" and grid[i + 1][j + 1] == "M")
                        or (grid[i - 1][j - 1] == "M" and grid[i + 1][j + 1] == "S")
                    ) and (
                        (grid[i - 1][j + 1] == "S" and grid[i + 1][j - 1] == "M")
                        or (grid[i - 1][j + 1] == "M" and grid[i + 1][j - 1] == "S")
                    ):
                        result2 += 1

        return result1, result2


solver = Solution()
print(solver.solve("2024/q4.txt"))
