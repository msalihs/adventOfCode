class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")

        lines = [line.strip("\n") for line in f.readlines()]

        def parse_instruction(line):
            i = 0
            result = 0
            needle = "mul("

            while i < len(line):
                while i < len(line) and line[i : i + len(needle)] != needle:
                    i += 1
                j = i + len(needle)
                while j < len(line) and line[j] != ")":
                    j += 1
                if j < len(line):
                    try:
                        nums = [int(x) for x in line[i + len(needle) : j].split(",")]
                        if len(nums) == 2:
                            result += nums[0] * nums[1]
                    except ValueError:
                        pass
                i = i + 1

            return result

        # Part 1
        for line in lines:
            result1 += parse_instruction(line)

        # Part 2
        curr_do = True
        for part in lines:
            lines = part.split("don't()")
            for idx, line in enumerate(lines):
                if not curr_do or idx > 0:
                    subline = line.split("do()")
                    if len(subline) > 1:
                        line = "".join(subline[1:])
                        curr_do = True
                    else:
                        curr_do = False
                        continue

                result2 += parse_instruction(line)

        return result1, result2


solver = Solution()
print(solver.solve("2024/q3.txt"))
