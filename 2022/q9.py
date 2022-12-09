from pathlib import Path
from collections import defaultdict


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = set(), 0
        readings = f.read().split("\n")
        instructions = [(r.split(" ")[0], int(r.split(" ")[1])) for r in readings]

        s, h, t = [0, 0], [0, 0], [0, 0]
        result1 = {(0, 0)}
        movement = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
        for dir, length in instructions:
            dx, dy = movement[dir]
            while length:
                h[0], h[1] = h[0] + dx, h[1] + dy
                if not (
                    (h[0] - 1) <= t[0] <= (h[0] + 1)
                    and (h[1] - 1) <= t[1] <= (h[1] + 1)
                ):
                    t[0] = h[0] - dx
                    t[1] = h[1] - dy
                    result1.add(tuple(t))
                length -= 1

        s, rope = [0, 0], [[0, 0] for _ in range(10)]
        result2 = {(0, 0)}
        movement = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
        for dir, length in instructions:
            dx, dy = movement[dir]
            while length:
                rope[0][0], rope[0][1] = rope[0][0] + dx, rope[0][1] + dy
                for i in range(1, 10):
                    if not (
                        (rope[i - 1][0] - 1) <= rope[i][0] <= (rope[i - 1][0] + 1)
                        and (rope[i - 1][1] - 1) <= rope[i][1] <= (rope[i - 1][1] + 1)
                    ):
                        if rope[i - 1][0] == rope[i][0]:
                            rope[i][1] += 1 if rope[i - 1][1] > rope[i][1] else -1
                        elif rope[i - 1][1] == rope[i][1]:
                            rope[i][0] += 1 if rope[i - 1][0] > rope[i][0] else -1
                        else:
                            di = rope[i - 1][0] - rope[i][0]
                            dj = rope[i - 1][1] - rope[i][1]
                            if abs(di) > 1:
                                di = 1 if di > 0 else -1
                            if abs(dj) > 1:
                                dj = 1 if dj > 0 else -1
                            rope[i][0] += di
                            rope[i][1] += dj
                        if not (
                            (rope[i - 1][0] - 1) <= rope[i][0] <= (rope[i - 1][0] + 1)
                            and (rope[i - 1][1] - 1)
                            <= rope[i][1]
                            <= (rope[i - 1][1] + 1)
                        ):
                            raise ValueError(i, di, dj, rope, dx, dy)
                result2.add(tuple(rope[-1]))
                length -= 1

        return len(result1), len(result2)


solver = Solution()
print(solver.solve("2022/q9.txt"))
