import math


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        readings = f.read().split("\n")

        instructions = list(readings[0])
        graph = dict()
        for reading in readings[2:]:
            node, nei = reading.split(" = ")
            l, r = nei.split(", ")
            graph[node] = {"L": l[1:], "R": r[:-1]}

        curr, finish = "AAA", "ZZZ"
        result1 = 0
        while curr != finish:
            curr = graph[curr][instructions[result1 % len(instructions)]]
            result1 += 1

        starts = [node for node in graph if node[-1] == "A"]
        results = list()
        for node in starts:
            i = 0
            while node[-1] != "Z":
                node = graph[node][instructions[i % len(instructions)]]
                i += 1
            results.append(i)
        result2 = math.lcm(*results)

        return result1, result2


solver = Solution()
print(solver.solve("2023/q8.txt"))
