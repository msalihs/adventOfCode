import heapq


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        elf_cals = [[]]
        for line in f.readlines():
            line = line.strip("\n")
            if line:
                elf_cals[-1].append(int(line))
            else:
                elf_cals.append([])

        cal_sums = list()
        for calories in elf_cals:
            _sum = sum(calories)
            heapq.heappush(cal_sums, -_sum)

        result1 = -cal_sums[0]
        result2 = -sum([heapq.heappop(cal_sums) for _ in range(3)])

        return result1, result2


solver = Solution()
print(solver.solve("2022/q1.txt"))
