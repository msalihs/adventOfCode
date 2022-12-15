import copy


class Solution:
    def __init__(self):
        pass

    def get_next_pos(self, blocked, lowest):
        x, y = 500, 0
        while True:
            while (x, y + 1) not in blocked and y < lowest:
                y = y + 1
            if (x - 1, y + 1) not in blocked and y < lowest:
                x, y = x - 1, y + 1
            elif (x + 1, y + 1) not in blocked and y < lowest:
                x, y = x + 1, y + 1
            else:
                break
        return (x, y)

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 1
        readings = f.read().split("\n")
        rock_pos = set()
        lowest = 0

        for reading in readings:
            for i, r in enumerate(reading.split(" -> ")):
                if i == 0:
                    x, y = [int(x) for x in r.split(",")]
                    continue
                xp, yp = [int(x) for x in r.split(",")]
                dx, dy = xp - x, yp - y
                l = abs(dx + dy)
                rock_pos |= {(x + i * dx // l, y + i * dy // l) for i in range(l + 1)}
                lowest = max([lowest, y, y + dy])
                x, y = xp, yp

        blocked = copy.deepcopy(rock_pos)
        x, y = self.get_next_pos(blocked, lowest)
        while y != lowest:
            blocked.add((x, y))
            result1 += 1
            x, y = self.get_next_pos(blocked, lowest)

        blocked = copy.deepcopy(rock_pos)
        lowest = lowest + 1
        x, y = self.get_next_pos(blocked, lowest)
        while (x, y) != (500, 0):
            blocked.add((x, y))
            result2 += 1
            x, y = self.get_next_pos(blocked, lowest)

        return result1, result2


solver = Solution()
print(solver.solve("2022/q14.txt"))
