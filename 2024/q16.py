import heapq


class Solution:
    def __init__(self, debug=False):
        self.debug = debug

    def solve(self, filepath):
        result1, result2 = 10 ** 10, 0
        f = open(filepath, "r")
        _input = f.read().split("\n")

        grid = [list(line) for line in _input]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "S":
                    start = (i, j)
                if grid[i][j] == "E":
                    end = (i, j)

        queue = [(0, start[0], start[1], 0, 1)]
        idx = 0
        happens = 0
        seen = {(start[0], start[1], 0, 1): 0}
        while queue:
            idx += 1
            cost, i, j, di, dj = heapq.heappop(queue)

            if (
                grid[i + di][j + dj] != "#"
                and seen.get((i + di, j + dj, di, dj), 10 ** 10) > cost + 1
            ):
                heapq.heappush(queue, (cost + 1, i + di, j + dj, di, dj))
                seen[(i + di, j + dj, di, dj)] = cost + 1
                if (i + di, j + dj) == end:
                    result1 = min(cost + 1, result1)
                    happens += 1
            if seen.get((i, j, dj, di), 10 ** 10) > cost + 1000:
                heapq.heappush(queue, (cost + 1000, i, j, dj, di))
                seen[(i, j, dj, di)] = cost + 1000
            if seen.get((i, j, -dj, -di), 10 ** 10) > cost + 1000:
                heapq.heappush(queue, (cost + 1000, i, j, -dj, -di))
                seen[(i, j, -dj, -di)] = cost + 1000

        queue = [end]
        result2 += 1
        visited = {end}
        while queue:
            i, j = queue.pop()
            min_val = result1
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                for ddi, ddj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    min_val = min(
                        min_val, seen.get((i + di, j + dj, ddi, ddj), 10 ** 10)
                    )

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                for ddi, ddj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if (
                        seen.get((i + di, j + dj, ddi, ddj), 10 ** 10) == min_val
                        and (i + di, j + dj) not in visited
                    ):
                        visited.add((i + di, j + dj))
                        queue.append((i + di, j + dj))
                        result2 += 1

        return result1, result2


solver = Solution()
print(solver.solve("2024/q16.txt"))
