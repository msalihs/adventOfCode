class Solution:
    def __init__(self):
        self.cache = {}

    def print_grid(self, grid):
        for i in range(len(grid)):
            print(grid[i])

    def get_load(self, grid):
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "O":
                    result += len(grid) - i
        return result

    def tilt(self, grid, dir):
        if dir == "N":
            for j in range(len(grid[0])):
                # print(j)
                i = len(grid) - 1
                count = 0
                while i >= 0:
                    if grid[i][j] == "#":
                        while count:
                            grid[i + count][j] = "O"
                            count -= 1
                    elif grid[i][j] == "O":
                        count += 1
                        grid[i][j] = "."
                    i -= 1
                while count:
                    grid[i + count][j] = "O"
                    count -= 1
        elif dir == "S":
            for j in range(len(grid[0])):
                # print(j)
                i = 0
                count = 0
                while i < len(grid):
                    if grid[i][j] == "#":
                        while count:
                            grid[i - count][j] = "O"
                            count -= 1
                    elif grid[i][j] == "O":
                        count += 1
                        grid[i][j] = "."
                    i += 1
                while count:
                    grid[i - count][j] = "O"
                    count -= 1
        elif dir == "E":
            for i in range(len(grid)):
                j = 0
                count = 0
                while j < len(grid):
                    if grid[i][j] == "#":
                        while count:
                            grid[i][j - count] = "O"
                            count -= 1
                    elif grid[i][j] == "O":
                        count += 1
                        grid[i][j] = "."
                    j += 1
                while count:
                    grid[i][j - count] = "O"
                    count -= 1
        if dir == "W":
            for i in range(len(grid)):
                # print(j)
                j = len(grid[0]) - 1
                count = 0
                while j >= 0:
                    if grid[i][j] == "#":
                        while count:
                            grid[i][j + count] = "O"
                            count -= 1
                    elif grid[i][j] == "O":
                        count += 1
                        grid[i][j] = "."
                    j -= 1
                while count:
                    grid[i][j + count] = "O"
                    count -= 1
        return grid

    def cycle(self, grid, n):
        first_cache_hit = -1
        i = 0
        while i < n:
            if isinstance(grid, str):
                pre_key = grid
            else:
                pre_key = "$".join(["".join(row) for row in grid])
            if pre_key not in self.cache:
                for dir in ["N", "W", "S", "E"]:
                    grid = self.tilt(grid, dir)
                post_key = "$".join(["".join(row) for row in grid])
                self.cache[pre_key] = post_key
            else:
                grid = self.cache[pre_key]
                if first_cache_hit == -1:
                    first_cache_hit = i
                    first_cache_key = pre_key
                elif pre_key == first_cache_key:
                    diff = i - first_cache_hit
                    i = n - ((n - i) % diff) + 1
                    continue
            i += 1

        if isinstance(grid, str):
            grid = [list(row) for row in grid.split("$")]

        return grid

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        grid = [list(reading) for reading in f.read().split("\n")]
        result1 = self.get_load(self.tilt(grid, "N"))
        result2 = self.get_load(self.cycle(grid, 1000000000))
        return result1, result2


solver = Solution()
print(solver.solve("2023/q14.txt"))
