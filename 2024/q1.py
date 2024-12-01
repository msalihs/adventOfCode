class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        input = [line.strip("\n") for line in f.readlines()]

        left_nums = []
        right_nums = []

        for num in input:
            left_nums.append(int(num.split(" ")[0]))
            right_nums.append(int(num.split(" ")[-1]))

        left_nums.sort()
        right_nums.sort()

        for x, y in zip(left_nums, right_nums):
            result1 += abs(x - y)

        counts = {}
        for num in right_nums:
            counts[num] = counts.get(num, 0) + 1

        for num in left_nums:
            result2 += num * counts.get(num, 0)

        return result1, result2


solver = Solution()
print(solver.solve("2024/q1.txt"))
