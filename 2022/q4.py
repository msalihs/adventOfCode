class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0

        pairs = []
        for line in f.readlines():
            line = line.strip("\n")
            ranges = line.split(",")
            pairs.append(
                tuple([[int(x) for x in range.split("-")] for range in ranges])
            )

        for p1, p2 in pairs:
            if (p1[0] <= p2[0] and p2[1] <= p1[1]) or (
                p2[0] <= p1[0] and p1[1] <= p2[1]
            ):
                result1 += 1

        for p1, p2 in pairs:
            if not (p1[1] < p2[0] or p2[1] < p1[0]):
                result2 += 1

        return result1, result2


solver = Solution()
print(solver.solve("2022/q4.txt"))
