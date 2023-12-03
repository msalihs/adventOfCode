import itertools


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        readings = f.read().split("\n")
        gears = dict()
        for i in range(len(readings)):
            j = 0
            while j < len(readings[i]):
                number = 0
                if not readings[i][j].isnumeric():
                    j += 1
                else:
                    begin = j
                    while j < len(readings[i]) and readings[i][j].isnumeric():
                        number = number * 10 + int(readings[i][j])
                        j += 1
                    k = j - 1
                    valid = False
                    while not valid and begin <= k:
                        for di, dj in itertools.product([-1, 0, 1], [-1, 0, 1]):
                            if (
                                0 <= i + di < len(readings)
                                and 0 <= k + dj < len(readings[i])
                                and not readings[i + di][k + dj].isnumeric()
                                and readings[i + di][k + dj] != "."
                            ):
                                valid = True
                                if readings[i + di][k + dj] == "*":
                                    if (i + di, k + dj) in gears:
                                        gears[(i + di, k + dj)].append(number)
                                    else:
                                        gears[(i + di, k + dj)] = [number]
                        k -= 1
                    if valid:
                        result1 += number

        for k, v in gears.items():
            if len(v) == 2:
                result2 += v[0] * v[1]

        return result1, result2


solver = Solution()
print(solver.solve("2023/q3.txt"))
