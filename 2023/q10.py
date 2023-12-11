from collections import defaultdict, deque


class Solution:
    def __init__(self):
        self.pipes = {
            "-": ((0, -1), (0, 1)),
            "|": ((-1, 0), (1, 0)),
            "L": ((0, 1), (-1, 0)),
            "J": ((-1, 0), (0, -1)),
            "7": ((1, 0), (0, -1)),
            "F": ((1, 0), (0, 1)),
            ".": ((0, 0), (0, 0)),
            "S": ((0, 1), (0, -1), (1, 0), (-1, 0)),
        }

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        readings = f.read().split("\n")
        grid = [list(reading) for reading in readings]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "S":
                    start = (i, j)

        queue = deque([(start, 0)])
        seen = dict()
        loop = {start}
        print(queue)
        while queue:
            # print(queue)
            (i, j), d = queue.popleft()
            seen[(i, j)] = d
            for di, dj in self.pipes[grid[i][j]]:
                if (
                    0 <= i + di < len(grid)
                    and 0 <= j + dj < len(grid[0])
                    and (i + di, j + dj) not in seen
                ):
                    if (-di, -dj) in self.pipes[grid[i + di][j + dj]]:
                        queue.append(((i + di, j + dj), d + 1))
        result1 = d
        queue = deque([(i, j)])
        while queue:
            (i, j) = queue.popleft()
            loop.add((i, j))
            for di, dj in self.pipes[grid[i][j]]:
                if (
                    0 <= i + di < len(grid)
                    and 0 <= j + dj < len(grid[0])
                    and (i + di, j + dj) not in loop
                ):
                    queue.append((i + di, j + dj))

        new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i, j in loop:
            new_grid[i][j] = 1

        for i in range(len(grid)):
            print(new_grid[i])
        row_prefix_sum = defaultdict(list)
        column_prefix_sum = defaultdict(list)

        for i in range(len(grid)):
            sum_ = 0
            for j in range(len(grid[0])):
                sum_ += new_grid[i][j]
                row_prefix_sum[i].append(sum_)

        for j in range(len(grid[0])):
            sum_ = 0
            for i in range(len(grid)):
                sum_ += new_grid[i][j]
                column_prefix_sum[j].append(sum_)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) == (4, 12):
                    print(i, j, new_grid[i][j])
                    print(row_prefix_sum)
                    print(column_prefix_sum)
                    print(((row_prefix_sum[i][j] - 0) % 2))
                if (
                    new_grid[i][j] == 0
                    and ((row_prefix_sum[i][j] - 0) % 2)
                    and ((row_prefix_sum[i][-1] - row_prefix_sum[i][j]) % 2)
                    and ((column_prefix_sum[j][i] - 0) % 2)
                    and ((column_prefix_sum[j][-1] - column_prefix_sum[j][i]) % 2)
                ):
                    result2 += 1

        return result1, result2


solver = Solution()
print(solver.solve("2023/q10.txt"))
