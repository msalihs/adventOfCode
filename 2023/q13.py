class Solution:
    def __init__(self):
        pass

    def find_max_reflextion(self, grids, fix_smudge=False):
        results = list()
        for grid in grids:
            max_di, max_i = 1, (-1, 0)
            for i in range(1, len(grid)):
                di = 1
                if fix_smudge:
                    max_fix = 1
                    while 0 <= i - di and (i + di - 1) < len(grid):
                        diff = 0
                        for c1, c2 in zip(grid[i - di], grid[i + di - 1]):
                            if c1 != c2:
                                diff += 1
                        if diff > max_fix:
                            break
                        di += 1
                        max_fix -= diff
                else:
                    while (
                        0 <= i - di
                        and (i + di - 1) < len(grid)
                        and grid[i - di] == grid[i + di - 1]
                    ):
                        di += 1
                if di > max_di and (0 > (i - di) or (i + di - 1) == len(grid)):
                    if not fix_smudge or (fix_smudge and max_fix != 1):
                        max_di = di
                        max_i = (i, di * 2 * len(grid[0]))
            results.append(max_i)
        return results

    def solve(self, filepath):
        f = open(filepath, "r")
        readings = f.read().split("\n\n")
        horizontal_grids = [reading.split("\n") for reading in readings]
        vertical_grids = [[*zip(*grid)] for grid in horizontal_grids]
        results = list()
        for fix_smudge in [False, True]:
            h_results = self.find_max_reflextion(
                horizontal_grids, fix_smudge=fix_smudge
            )
            v_results = self.find_max_reflextion(vertical_grids, fix_smudge=fix_smudge)
            result = 0
            for i, ((h_i, h_diff), (v_i, v_diff)) in enumerate(
                zip(h_results, v_results)
            ):
                result += h_i * 100 if h_diff > v_diff else v_i
            results.append(result)
        return tuple(results)


solver = Solution()
print(solver.solve("2023/q13.txt"))
