class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        readings = f.read().strip("\n")

        i, k = 0, 4
        while len(set(readings[i : i + k])) != k:
            i += 1
        result1 = i + k

        i, k = 0, 14
        while len(set(readings[i : i + 14])) != 14:
            i += 1
        result2 = i + 14

        return result1, result2


solver = Solution()
print(solver.solve("2022/q6.txt"))
