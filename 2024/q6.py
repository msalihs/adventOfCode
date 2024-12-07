class Solution:
    def _init_(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        grid = [list(l) for l in f.read().split("\n") if len(l) > 0]
        n, m = len(grid), len(grid[0])
        dirs = ["^", ">", "v", "<"]
        dirs_delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        curr, i = None, 0
        while curr is None and i < n:
            for j in range(m):
                if grid[i][j] == dirs[0]:
                    si, sj = i, j
                    break
            i += 1

        def get_path(si, sj, map):
            x, y = si, sj
            dir_idx = 0
            seen = {(x, y, dirs[dir_idx])}
            while True:
                dx, dy = dirs_delta[dir_idx]

                while (
                    x + dx >= 0
                    and x + dx < n
                    and y + dy >= 0
                    and y + dy < m
                    and map[x + dx][y + dy] != "#"
                ):
                    x, y = x + dx, y + dy
                    if (x, y, dirs[dir_idx]) in seen:
                        raise Exception("Loop detected")
                    seen.add((x, y, dirs[dir_idx]))

                if x + dx >= 0 and x + dx < n and y + dy >= 0 and y + dy < m:
                    dir_idx = (dir_idx + 1) % len(dirs)
                else:
                    break

            return seen

        # PART 1
        exact_path = get_path(si, sj, grid)
        unique_path = {(x, y) for (x, y, d) in exact_path}
        result1 = len(unique_path)

        # PART 2
        for i, j in unique_path:
            grid[i][j] = "#"
            try:
                get_path(si, sj, grid)
            except:
                result2 += 1
            grid[i][j] = "."

        return result1, result2


solver = Solution()
print(solver.solve("2024/q6.txt"))
