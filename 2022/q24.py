from collections import defaultdict, deque


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        grid = [list(r) for r in f.read().split("\n")]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        blizzard = defaultdict(list)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] not in {"#", "."}:
                    blizzard[(i, j)].append(grid[i][j])

        start, end = (-1, -1), (-1, -1)
        for j in range(len(grid[0])):
            if grid[0][j] == ".":
                start = (0, j)
                break

        for j in reversed(range(len(grid[-1]))):
            if grid[-1][j] == ".":
                end = (len(grid) - 1, j)
                break

        starts = [start, end, start]
        targets = [end, start, end]
        t = 0
        blizzards = {0: blizzard}
        m = 1000000
        seen = set()
        results = list()
        for s, e in zip(starts, targets):
            queue = deque([(*s, t)])
            seen.add((*s, t))
            while queue:
                i, j, t = queue.popleft()
                if (t + 1) % m not in blizzards:
                    blizzards[t + 1] = defaultdict(list)
                    for k, l in blizzards[t]:
                        for dir in blizzards[t][(k, l)]:
                            if dir == ">":
                                if l >= (len(grid[0]) - 2):
                                    blizzards[t + 1][(k, 1)].append(dir)
                                else:
                                    blizzards[t + 1][(k, l + 1)].append(dir)
                            elif dir == "<":
                                if l < 2:
                                    blizzards[t + 1][(k, len(grid[0]) - 2)].append(dir)
                                else:
                                    blizzards[t + 1][(k, l - 1)].append(dir)
                            elif dir == "^":
                                if k < 2:
                                    blizzards[t + 1][(len(grid) - 2, l)].append(dir)
                                else:
                                    blizzards[t + 1][(k - 1, l)].append(dir)
                            elif dir == "v":
                                if k >= (len(grid) - 2):
                                    blizzards[t + 1][(1, l)].append(dir)
                                else:
                                    blizzards[t + 1][(k + 1, l)].append(dir)
                    if blizzards[t + 1] == blizzards[0]:
                        m = t + 1
                        print(f"Found modulo {m}")

                    for k, l in blizzards[t + 1]:
                        assert k < (len(grid) - 1) and l < (len(grid[0]) - 1)
                for di, dj in dirs:
                    if (
                        0 <= i + di < len(grid)
                        and 0 <= j + dj < len(grid[0])
                        and (i + di, j + dj) not in blizzards[(t + 1) % m]
                        and grid[i + di][j + dj] != "#"
                    ):
                        if (i + di, j + dj) == e:
                            results.append(t + 1)
                            break
                        elif (i + di, j + dj, t + 1) not in seen:
                            queue.append((i + di, j + dj, t + 1))
                            seen.add((i + di, j + dj, t + 1))
                else:
                    if (i, j) not in blizzards[(t + 1) % m] and (i, j, t + 1) not in seen:
                        queue.append((i, j, t + 1))
                        seen.add((i, j, t + 1))
                    continue
                break

        result1 = results[0]
        result2 = results[-1]

        return result1, result2


solver = Solution()
print(solver.solve("2022/q24.txt"))
