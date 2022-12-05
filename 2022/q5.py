from collections import defaultdict
from collections import deque
import copy


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        k = 9
        stacks = defaultdict(deque)

        readings = f.read().split("\n\n")

        for line in readings[0].split("\n"):
            print(line)
            line = line.strip("\n")
            if not line:
                break
            if "1" in line:
                continue
            for i in range(k):
                if line[i * 4 + 1] != " ":
                    stacks[i + 1].append(line[i * 4 + 1])

        stacks2 = copy.deepcopy(stacks)

        instructions = []
        for line in readings[1].split("\n"):
            instructions.append([int(c) for c in line.split(" ") if c.isnumeric()])

        for quantity, source, dest in instructions:
            for i in range(quantity):
                stacks[dest].appendleft(stacks[source].popleft())

        result1 = "".join([stacks[i + 1][0] for i in range(k)])

        for quantity, source, dest in instructions:
            for i in range(quantity):
                stacks2[dest].insert(i, stacks2[source].popleft())

        result2 = "".join([stacks2[i + 1][0] for i in range(k)])

        return result1, result2


solver = Solution()
print(solver.solve("2022/q5.txt"))
