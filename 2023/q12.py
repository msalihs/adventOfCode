from collections import Counter


class Solution:
    def __init__(self):
        self.cache = dict()

    def search_valid(self, record, expected):
        result = 0
        key = ("".join(record), tuple(expected))
        if key in self.cache:
            return self.cache[key]
        if len(expected) == 0:
            return int("#" not in record)
        if not record and len(expected) != 0:
            return 0

        i = 0
        max_i = len(record) - sum(expected) - len(expected) + 2
        while i < max_i:
            n = expected[0]
            j = i

            while j < len(record) and record[j] == ".":
                j += 1
                i += 1
            while n and j < len(record):
                if record[j] == ".":
                    break
                j += 1
                n -= 1
            if n == 0 and (j == len(record) or (j < len(record) and record[j] != "#")):
                result += self.search_valid(record[j + 1 :], expected[1:])
                if record[i] != "#":
                    i += 1
                else:
                    break
            elif i < max_i and record[i] == "#":
                break
            else:
                i += 1
        self.cache[key] = result
        return result

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        readings = f.read().split("\n")
        conditions = [reading.split(" ") for reading in readings]

        for condition in conditions:
            condition[1] = [int(c) for c in condition[1].split(",")]

        for (r, e) in conditions:
            res = self.search_valid(list(r), e)
            result1 += res

        for (r, e) in conditions:
            r = "?".join([r] * 5)
            new_e = list()
            for _ in range(5):
                new_e += e
            res = self.search_valid(list(r), new_e)
            result2 += res

        return result1, result2


solver = Solution()
print(solver.solve("2023/q12.txt"))
