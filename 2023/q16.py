from collections import deque


class Solution:
    def __init__(self, filepath):
        f = open(filepath, "r")
        self.grid = [list(row) for row in f.read().split("\n") if row]

    def get_energized(self, start=(0, -1, 0, 1)):
        queue = deque([start])
        seen = set()
        while queue:
            i, j, di, dj = queue.popleft()
            if (i, j, di, dj) in seen:
                continue
            seen.add((i, j, di, dj))
            if 0 <= i + di < len(self.grid) and 0 <= j + dj < len(self.grid[0]):
                ip, jp = i + di, j + dj
                # GOING RIGHT, LEFT
                if di == 0:
                    if self.grid[ip][jp] == "|":
                        queue.append((ip, jp, 1, 0))
                        queue.append((ip, jp, -1, 0))
                    elif self.grid[ip][jp] == "\\":
                        queue.append((ip, jp, 1 if dj == 1 else -1, 0))
                    elif self.grid[ip][jp] == "/":
                        queue.append((ip, jp, -1 if dj == 1 else 1, 0))
                    else:
                        queue.append((ip, jp, di, dj))

                # GOING UP, DOWN
                if dj == 0:
                    if self.grid[ip][jp] == "-":
                        queue.append((ip, jp, 0, -1))
                        queue.append((ip, jp, 0, 1))
                    elif self.grid[ip][jp] == "\\":
                        queue.append((ip, jp, 0, 1 if di == 1 else -1))
                    elif self.grid[ip][jp] == "/":
                        queue.append((ip, jp, 0, -1 if di == 1 else 1))
                    else:
                        queue.append((ip, jp, di, dj))

        energized = set()
        for i, j, _, _ in seen:
            energized.add((i, j))
        # Remove imaginary start of (0, -1)
        return len(energized) - 1

    def solve(self):
        result1, result2 = 0, 0
        result1 = self.get_energized()

        for i in range(len(self.grid)):
            result2 = max(result2, self.get_energized((i, -1, 0, 1)))
            result2 = max(result2, self.get_energized((i, len(self.grid[0]), 0, -1)))
        for j in range(len(self.grid[0])):
            result2 = max(result2, self.get_energized((-1, j, 1, 0)))
            result2 = max(result2, self.get_energized((len(self.grid), j, -1, 0)))

        return result1, result2


solver = Solution("2023/q16.txt")
print(solver.solve())
