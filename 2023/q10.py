from collections import defaultdict, deque


class Solution:
    def __init__(self):
        self.pipes = {
            "-": {(0, -1), (0, 1)},
            "|": {(-1, 0), (1, 0)},
            "L": {(0, 1), (-1, 0)},
            "J": {(-1, 0), (0, -1)},
            "7": {(1, 0), (0, -1)},
            "F": {(1, 0), (0, 1)},
            ".": {(0, 0), (0, 0)},
            "S": {(0, 1), (0, -1), (1, 0), (-1, 0)},
        }

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        readings = f.read().split("\n")
        grid = [list(reading) for reading in readings if reading != ""]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "S":
                    s_i = i
                    s_j = j

        # Deduce what shape is S
        valid = set()
        for di, dj in self.pipes["S"]:
            if (
                0 <= s_i + di < len(grid)
                and 0 <= s_j + dj < len(grid[0])
                and (-di, -dj) in self.pipes[grid[s_i + di][s_j + dj]]
            ):
                valid.add((di, dj))

        for k, v in self.pipes.items():
            if v == valid:
                grid[s_i][s_j] = k

        # Perform BFS and the last element is the furthest.
        queue = deque([((s_i, s_j), 0)])
        loop = dict()
        while queue:
            (i, j), d = queue.popleft()
            loop[(i, j)] = d
            for di, dj in self.pipes[grid[i][j]]:
                if (
                    0 <= i + di < len(grid)
                    and 0 <= j + dj < len(grid[0])
                    and (i + di, j + dj) not in loop
                ):
                    if (-di, -dj) in self.pipes[grid[i + di][j + dj]]:
                        queue.append(((i + di, j + dj), d + 1))
        result1 = d

        # Scan accross and find whether we're in or out by checking if we cross "|", "J" or "L"
        for i in range(len(grid)):
            inside = 0
            for j in range(len(grid[0])):
                if (i, j) in loop:
                    if grid[i][j] in {"|", "J", "L"}:
                        inside ^= 1
                else:
                    result2 += inside

        return result1, result2


solver = Solution()
print(solver.solve("2023/q10.txt"))
