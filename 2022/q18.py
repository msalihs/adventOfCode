class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2, cubes = 0, 0, set()
        minx, miny, minz, maxx, maxy, maxz = (
            10 ** 10,
            10 ** 10,
            10 ** 10,
            -(10 ** 10),
            -(10 ** 10),
            -(10 ** 10),
        )
        for reading in f.read().split("\n"):
            x, y, z = [int(num) for num in reading.split(",")]
            cubes.add((x, y, z))
            minx, miny, minz = min(minx, x), min(miny, y), min(minz, z)
            maxx, maxy, maxz = max(maxx, x), max(maxy, y), max(maxz, z)

        for x, y, z in cubes:
            for dx, dy, dz in [
                (1, 0, 0),
                (-1, 0, 0),
                (0, 1, 0),
                (0, -1, 0),
                (0, 0, 1),
                (0, 0, -1),
            ]:
                k = x + dx, y + dy, z + dz
                if k not in cubes:
                    result1 += 1

        surface = set()

        for x, y, z in cubes:
            for dx, dy, dz in [
                (1, 0, 0),
                (-1, 0, 0),
                (0, 1, 0),
                (0, -1, 0),
                (0, 0, 1),
                (0, 0, -1),
            ]:
                k = x + dx, y + dy, z + dz
                if k in cubes:
                    continue
                seen = set()
                queue = [k]
                while queue:
                    xk, yk, zk = queue.pop()
                    if (xk, yk, zk) in seen:
                        continue
                    seen.add((xk, yk, zk))
                    if (
                        (xk, yk, zk) in surface
                        or (minx > xk or xk > maxx)
                        or (miny > yk or yk > maxy)
                        or (minz > zk or zk > maxz)
                    ):
                        surface |= seen - cubes
                        break
                    if (xk, yk, zk) not in cubes:
                        for ddx, ddy, ddz in [
                            (1, 0, 0),
                            (-1, 0, 0),
                            (0, 1, 0),
                            (0, -1, 0),
                            (0, 0, 1),
                            (0, 0, -1),
                        ]:
                            queue.append((xk + ddx, yk + ddy, zk + ddz))
                else:
                    continue
                result2 += 1
        print(len(surface))

        return result1, result2


solver = Solution()
print(solver.solve("2022/q18.txt"))
