from collections import deque


class Solution:
    def __init__(self):
        self.queue = deque([])
        self.seen = set()
        self.grid = list()
        self.start, self.target = (0, 0), (0, 0)

    def get_shortest_path(self):
        while self.queue:
            (i, j), l = self.queue.popleft()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (i + di, j + dj) in self.seen:
                    continue
                if (
                    0 <= (i + di) < len(self.grid)
                    and 0 <= (j + dj) < len(self.grid[0])
                    and self.grid[i][j] + 1 >= self.grid[i + di][j + dj]
                ):
                    if (i + di, j + dj) == self.target:
                        return l + 1
                    self.seen.add((i + di, j + dj))
                    self.queue.append(((i + di, j + dj), l + 1))
        return -1

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        readings = f.read().split("\n")
        self.grid = [list(reading) for reading in readings]

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == "S":
                    self.start = (i, j)
                if self.grid[i][j] == "E":
                    self.target = (i, j)

        self.grid = [[ord(c) - ord("a") for c in reading] for reading in readings]
        self.grid[self.start[0]][self.start[1]] = 0
        self.grid[self.target[0]][self.target[1]] = ord("z") - ord("a")

        self.queue = deque([(self.start, 0)])
        self.seen = {self.start}
        result1 = self.get_shortest_path()

        self.queue = deque([])
        self.seen = set()

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 0:
                    self.queue.append(((i, j), 0))
                    self.seen.add((i, j))

        result2 = self.get_shortest_path()

        return result1, result2


solver = Solution()
print(solver.solve("2022/q12.txt"))
