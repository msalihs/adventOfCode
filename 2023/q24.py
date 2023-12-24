from z3 import *


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        hailstones = list()

        for reading in f.read().split("\n"):
            if reading:
                pos, vel = reading.split(" @ ")
                hailstones.append(
                    (
                        (
                            tuple([int(x) for x in pos.split(", ")]),
                            tuple([int(x) for x in vel.split(", ")]),
                        )
                    )
                )

        # print(hailstones)
        min_ = 200000000000000
        max_ = 400000000000000
        for i in range(len(hailstones)):
            (x1, y1, z1), (dx1, dy1, dz1) = hailstones[i]
            for j in range(i + 1, len(hailstones)):
                (x2, y2, z2), (dx2, dy2, dz2) = hailstones[j]
                m1 = dy1 / dx1
                m2 = dy2 / dx2
                b1 = y1 - m1 * x1
                b2 = y2 - m2 * x2
                if m1 == m2:
                    continue
                xp = (b2 - b1) / (m1 - m2)
                yp = m1 * xp + b1
                # print(xp, yp)
                if min_ <= xp <= max_ and min_ <= yp <= max_:
                    t1 = (xp - x1) / dx1
                    t2 = (xp - x2) / dx2
                    if t1 > 0 and t2 > 0:
                        result1 += 1

        # USE z3 to solve SAT problem
        solver = Solver()
        Xp, dXp = Int("Xp"), Int("dXp")
        Yp, dYp = Int("Yp"), Int("dYp")
        Zp, dZp = Int("Zp"), Int("dZp")

        for idx, ((x, y, z), (dx, dy, dz)) in enumerate(hailstones):
            t = Int(f"{idx}")
            solver.add(t >= 0)
            solver.add(x + dx * t == Xp + dXp * t)
            solver.add(y + dy * t == Yp + dYp * t)
            solver.add(z + dz * t == Zp + dZp * t)

        print(f'Solver check returned "{solver.check()}"')
        result2 = solver.model().eval(Xp + Yp + Zp)

        return result1, result2


solver = Solution()
print(solver.solve("2023/q24.txt"))
