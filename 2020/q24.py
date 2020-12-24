class Solution:
    def __init__(self):
        pass

    def parse_file(self, filepath):
        f = open(filepath, "r")
        instructions = list()
        for line in f.readlines():
            line = line.strip("\n")
            index = 0
            instruction = list()
            while index < len(line):
                c = line[index]
                if c == "e" or c == "w":
                    instruction.append(c)
                    index += 1
                else:
                    instruction.append(line[index : index + 2])
                    index += 2
            instructions.append(instruction)
        return instructions

    def solve(self, filepath):
        result1, result2 = 0, 0
        allInstructions = self.parse_file(filepath)
        print(allInstructions[0])
        reference = (0, 0)
        deltas = {
            "e": (2, 0),
            "w": (-2, 0),
            "ne": (1, 1),
            "nw": (-1, 1),
            "se": (1, -1),
            "sw": (-1, -1),
        }
        allNodes = dict()

        for instructions in allInstructions:
            point = list(reference)
            for instruction in instructions:
                dx, dy = deltas[instruction]
                point[0] += dx
                point[1] += dy
            allNodes[tuple(point)] = allNodes.get(tuple(point), 0) ^ 1

        result1 = sum([color for node, color in allNodes.items()])

        # PART 2
        allBlack = {x for x, c in allNodes.items() if c == 1}
        for _ in range(100):
            nextAllBlack = set()
            counts = dict()
            for x, y in allBlack:
                for ins, (dx, dy) in deltas.items():
                    neighbor = (x + dx, y + dy)
                    counts[neighbor] = counts.get(neighbor, 0) + 1
            for node, count in counts.items():
                if (node in allBlack and (count == 1 or count == 2)) or (
                    node not in allBlack and count == 2
                ):
                    nextAllBlack.add(node)
            allBlack = nextAllBlack.copy()
        result2 = len(allBlack)

        return result1, result2


solver = Solution()
print(solver.solve("2020/q24.txt"))
