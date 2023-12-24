from collections import deque
import sys

# print(sys.getrecursionlimit())
sys.setrecursionlimit(3000)
# print(sys.getrecursionlimit())


class Solution:
    def __init__(self):
        self.slopes = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        grid = [list(row) for row in f.read().split("\n") if row]
        # for i in range(len(grid)):
        #     print(grid[i])

        for j in range(len(grid[0])):
            if grid[0][j] == ".":
                break

        si, sj = 0, j

        for j in range(len(grid[0])):
            if grid[-1][j] == ".":
                break
        fi, fj = len(grid) - 1, j
        # size = len(grid) * len(grid[0])
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == '#':
        #             size -= 1

        # print(size)

        counter = dict()
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] != "#":
                    count = 0
                    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if grid[i + di][j + dj] == "#":
                            count += 1
                    if count == 0:
                        print(i, j)
                    counter[count] = counter.get(count, 0) + 1

        print(counter)

        def helper(i, j, d, s, icy=True):
            result = -1
            if (i, j) == (fi, fj):
                # print(d)
                return d
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ip, jp = i + di, j + dj
                if (
                    0 <= ip < len(grid)
                    and 0 <= jp < len(grid[0])
                    and grid[ip][jp] != "#"
                ):
                    if icy:
                        ts = s
                        if grid[ip][jp] != ".":
                            slope_di, slope_dj = self.slopes[grid[ip][jp]]
                            if slope_di == -di and slope_dj == -dj:
                                ts = s + 1
                            else:
                                ts = 0
                    else:
                        ts = 0
                    if ts < 2:
                        original = grid[ip][jp]
                        grid[ip][jp] = "#"
                        result = max(result, helper(ip, jp, d + 1, ts))
                        grid[ip][jp] = original
            return result

        result1 = helper(si, sj, 0, 0)

        queue = deque([(si, sj)])
        graph = {(si, sj): dict()}
        seen = {(si, sj)}
        while queue:
            node = queue.popleft()
            i, j = node
            d = 0
            while True:
                valid = set()
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ip, jp = i + di, j + dj
                    if (
                        0 <= ip < len(grid)
                        and 0 <= jp < len(grid[0])
                        and grid[ip][jp] != "#"
                    ):
                        valid.add((di, dj))
                d += 1
                if len(valid) > 1:
                    for next_node in valid:
                        queue.append((next_node, node))
                        graph[node][next_node] = d
                        seen.add(next_node)
                    break
                else:
                    i, j = valid.pop()

        result2 = helper(si, sj, 0, 0)

        return result1, result2


solver = Solution()
print(solver.solve("2023/q23.txt"))
