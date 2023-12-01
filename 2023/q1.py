import heapq


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        input_ = [line.strip("\n") for line in f.readlines()]

        for line in input_:
            l, r = 0, len(line) - 1
            while not line[l].isdigit():
                l += 1
            while not line[r].isdigit():
                r -= 1
            result1 += int(line[l]) * 10 + int(line[r])

        spellings = {
            0: "zero",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
        }

        for line in input_:
            l, r = 0, len(line) - 1
            while l < len(line):
                if line[l].isdigit():
                    result2 += int(line[l]) * 10
                    break
                for k, v in spellings.items():
                    if line[l : l + len(v)] == v:
                        result2 += k * 10
                        l = len(line)
                        break
                l += 1

            while r > 0:
                if line[r].isdigit():
                    result2 += int(line[r])
                    break
                for k, v in spellings.items():
                    if line[r : r + len(v)] == v:
                        result2 += k
                        r = -1
                        break
                r -= 1

        return result1, result2

solver = Solution()
print(solver.solve("2023/q1.txt"))
