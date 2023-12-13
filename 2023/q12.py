class Solution:
    def __init__(self):
        self.cache = dict()

    def search_valid(self, record, expected):
        key = ("".join(record), tuple(expected))
        if key in self.cache:
            return self.cache[key]
        if len(expected) == 0:
            return int("#" not in record)
        if not record and len(expected) != 0:
            return 0

        i, result = 0, 0
        while i < len(record):
            n, j = expected[0], i
            while j < len(record) and record[j] == ".":
                i, j = i + 1, j + 1
            while n and j < len(record):
                if record[j] == ".":
                    break
                j, n = j + 1, n - 1
            if n == 0 and (j == len(record) or (j < len(record) and record[j] != "#")):
                result += self.search_valid(record[j + 1 :], expected[1:])
            if i < len(record) and record[i] == "#":
                break
            i += 1

        self.cache[key] = result
        return result

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        readings = f.read().split("\n")
        conditions = [reading.split(" ") for reading in readings if reading]

        for condition in conditions:
            condition[1] = [int(c) for c in condition[1].split(",")]

        for (r, e) in conditions:
            res = self.search_valid(list(r), e)
            result1 += res

        for (r, e) in conditions:
            res = self.search_valid(list("?".join([r] * 5)), e * 5)
            result2 += res

        return result1, result2


solver = Solution()
print(solver.solve("2023/q12.txt"))
