class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        grid = [line.strip("\n") for line in f.readlines()]

        n = len(grid)
        m = len(grid[0])

        # PART 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'X':
                    if grid[i][j:j+4] == 'XMAS':
                        result1 += 1
                            
                    if grid[i][j-3:j+1] == 'SAMX':
                        result1 += 1

                    if (i < n - 3):
                        if j < (m-3) and grid[i+1][j+1] == 'M' and grid[i+2][j+2] == 'A' and grid[i+3][j+3] == 'S':
                            result1 += 1

                        if j >= 3 and grid[i+1][j-1] == 'M' and grid[i+2][j-2] == 'A' and grid[i+3][j-3] == 'S':
                            result1 += 1

                        if grid[i+1][j] == 'M' and grid[i+2][j] == 'A' and grid[i+3][j] == 'S':
                            result1 += 1

                    if (i > 2):
                        if j >= 3 and grid[i-1][j-1] == 'M' and grid[i-2][j-2] == 'A' and grid[i-3][j-3] == 'S':
                            result1 += 1

                        if j < (m-3) and grid[i-1][j+1] == 'M' and grid[i-2][j+2] == 'A' and grid[i-3][j+3] == 'S':
                            result1 += 1

                        if grid[i-1][j] == 'M' and grid[i-2][j] == 'A' and grid[i-3][j] == 'S':
                            result1 += 1


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
