import math


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 1, 0
        readings = f.read().split("\n")
        times = [int(k) for k in readings[0].split(":")[1].split(" ") if k]
        distances = [int(k) for k in readings[1].split(":")[1].split(" ") if k]
        mapping = {k: v for k, v in zip(times, distances)}

        for t, d in mapping.items():
            count = 0
            for i in range(t):
                new_d = (t - i) * i
                if new_d > d:
                    count += 1
            result1 *= count

        new_t = int("".join([str(t) for t in times]))
        new_d = int("".join([str(t) for t in distances]))
        max_t = math.floor((new_t + (new_t ** 2 - 4 * new_d) ** 0.5) / 2)
        min_t = math.ceil((new_t - (new_t ** 2 - 4 * new_d) ** 0.5) / 2)
        result2 = max_t - min_t + 1
        return result1, result2


solver = Solution()
print(solver.solve("2023/q6.txt"))
