import copy


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        readings = f.read().split("\n")
        rocks = [
            [[int(x) for x in r.split(",")] for r in reading.split(" -> ")]
            for reading in readings
        ]
        rock_pos = set()
        lowest = 0
        for rock in rocks:
            for i in range(1, len(rock)):
                rock_pos.add(tuple(rock[i]))
                rock_pos.add(tuple(rock[i - 1]))
                lowest = max(lowest, rock[i][1])
                lowest = max(lowest, rock[i - 1][1])
                if rock[i][0] == rock[i - 1][0]:
                    diff = rock[i][1] - rock[i - 1][1]
                    while diff != 0:
                        rock_pos.add((rock[i][0], rock[i][1] - diff))
                        lowest = max(lowest, rock[i][1] - diff)
                        diff += 1 if diff < 0 else -1
                if rock[i][1] == rock[i - 1][1]:
                    diff = rock[i][0] - rock[i - 1][0]
                    while diff != 0:
                        rock_pos.add((rock[i][0] - diff, rock[i][1]))
                        diff += 1 if diff < 0 else -1

        blocked = copy.deepcopy(rock_pos)
        while True:
            x, y = 500, 0
            while True:
                while (x, y + 1) not in blocked and y < lowest:
                    y += 1
                if (x - 1, y + 1) not in blocked and y < lowest:
                    x -= 1
                    y += 1
                elif (x + 1, y + 1) not in blocked and y < lowest:
                    x += 1
                    y += 1
                else:
                    break

            if y == lowest:
                break
            blocked.add((x, y))
            result1 += 1

        blocked = copy.deepcopy(rock_pos)
        lowest = lowest + 1
        while True:
            x, y = 500, 0
            while True:
                while (x, y + 1) not in blocked and y < lowest:
                    y += 1
                if (x - 1, y + 1) not in blocked and y < lowest:
                    x -= 1
                    y += 1
                elif (x + 1, y + 1) not in blocked and y < lowest:
                    x += 1
                    y += 1
                else:
                    break

            if (x, y) == (500, 0):
                result2 += 1
                break
            blocked.add((x, y))
            result2 += 1

        return result1, result2


solver = Solution()
print(solver.solve("2022/q14.txt"))
