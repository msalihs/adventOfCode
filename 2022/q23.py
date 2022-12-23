from collections import defaultdict


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 1
        positions = [list(r) for r in f.read().split("\n")]
        valid_dirs = [
            ((-1, 0), (-1, 1), (-1, -1)),
            ((1, 0), (1, 1), (1, -1)),
            ((0, -1), (1, -1), (-1, -1)),
            ((0, 1), (1, 1), (-1, 1)),
        ]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        dir_idx = 0

        elves = set()
        for i in range(len(positions)):
            for j in range(len(positions[0])):
                if positions[i][j] == "#":
                    elves.add((i, j))

        while True:
            proposed = defaultdict(list)
            for (i, j) in elves:
                for di, dj in dirs:
                    if (i + di, j + dj) in elves:
                        break
                else:
                    continue
                np = None
                for k in range(len(valid_dirs)):
                    vd = valid_dirs[(dir_idx + k) % len(valid_dirs)]
                    for di, dj in vd:
                        if (i + di, j + dj) in elves:
                            break
                    else:
                        di, dj = vd[0]
                        np = (i + di, j + dj)
                        break
                if np:
                    proposed[np].append((i, j))

            if len(proposed) == 0:
                break

            for p in proposed:
                if len(proposed[p]) == 1:
                    elves.remove(proposed[p][0])
                    elves.add(p)

            dir_idx += 1
            result2 += 1

        min_i = min_j = 10 ** 10
        max_i = max_j = -(10 ** 10)
        for i, j in elves:
            min_i = min(min_i, i)
            min_j = min(min_j, j)
            max_i = max(max_i, i)
            max_j = max(max_j, j)

        result1 = (max_j - min_j + 1) * (max_i - min_i + 1) - len(elves)

        return result1, result2


solver = Solution()
print(solver.solve("2022/q23.txt"))
