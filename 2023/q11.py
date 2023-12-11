class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        readings = f.read().split("\n")

        def helper(weight):
            result = 0
            grid = [list(reading) for reading in readings]
            row_w = {i: 1 for i in range(len(grid))}
            column_w = {j: 1 for j in range(len(grid[0]))}
            galaxies = [
                (i, j)
                for j in range(len(grid))
                for i in range(len(grid))
                if grid[i][j] == "#"
            ]

            for i in range(len(grid)):
                if all([grid[i][j] != "#" for j in range(len(grid))]):
                    row_w[i] = weight

            for j in range(len(grid)):
                if all([grid[i][j] != "#" for i in range(len(grid))]):
                    column_w[j] = weight

            for i, (s_i, s_j) in enumerate(galaxies):
                for j, (e_i, e_j) in enumerate(galaxies[i + 1 :]):
                    d = 0
                    for di in range(min(s_i, e_i), max(s_i, e_i)):
                        d += row_w[di]
                    for dj in range(min(s_j, e_j), max(s_j, e_j)):
                        d += column_w[dj]
                    result += d
            return result

        result1 = helper(2)
        result2 = helper(10 ** 6)
        return result1, result2


solver = Solution()
print(solver.solve("2023/q11.txt"))
