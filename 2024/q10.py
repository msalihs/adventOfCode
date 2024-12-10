from collections import defaultdict


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        grid = [[int(c) for c in line.strip()] for line in f.readlines()]

        n, m = len(grid), len(grid[0])

        def search(x, y, unique_peak=True):
            queue = [(x, y)]
            seen = {(x, y)}
            if unique_peak:
                result = set()
            else:
                result = 0

            while queue:
                i, j = queue.pop()
                h = grid[i][j]
                for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    ip, jp = i + di, j + dj
                    if 0 <= ip < n and 0 <= jp < m and grid[ip][jp] == (h + 1):
                        if unique_peak and (ip, jp) not in seen:
                            if (h + 1) == 9:
                                result.add((ip, jp))
                            else:
                                queue.append((ip, jp))
                                seen.add((ip, jp))
                        elif not unique_peak:
                            if (h + 1) == 9:
                                result += 1
                            else:
                                queue.append((ip, jp))

            return len(result) if unique_peak else result

        # PART 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    result1 += search(i, j)

        # PART 2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    result2 += search(i, j, unique_peak=False)

        return result1, result2


solver = Solution()
print(solver.solve("2024/q10.txt"))
