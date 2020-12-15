class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        nums = list()

        for line in f.readlines():
            nums += [int(x) for x in line.split(",")]

        indices = {x: (i + 1) for i, x in enumerate(nums)}
        start = len(nums) + 1
        part1_end, part2_end = 2020, 30000000
        last = 0

        while start < part2_end:
            if last not in indices:
                indices[last] = start
                last = 0
            else:
                t = last
                last = start - indices[last]
                indices[t] = start
            start += 1

            if start == part1_end:
                result1 = last

        result2 = last

        return result1, result2


solver = Solution()
print(solver.solve("2020/q15.txt"))
