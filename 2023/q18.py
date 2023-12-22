from collections import Counter


class Solution:
    def __init__(self):
        self.real_dirs = {"0": (0, 1), "2": (0, -1), "1": (1, 0), "3": (-1, 0)}
        self.dirs = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}

    def shoelace(self, vertices, perimeter):
        result = 0
        for i in range(1, len(vertices)):
            (x0, y0), (x1, y1) = vertices[i - 1], vertices[i]
            result += x1 * y0 - y1 * x0
        return result // 2 + (perimeter // 2) + 1

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        readings = f.read().split("\n")
        instructions = [reading.split(" ") for reading in readings if reading]
        # print(instructions)

        pos = (0, 0)
        vertices = [pos]
        perimeter = 0
        for dir, l, real_instruction in instructions:
            di, dj = self.dirs[dir]
            pos = (pos[0] + di * int(l), pos[1] + dj * int(l))
            vertices.append(pos)
            perimeter += abs((di + dj) * int(l))

        result1 = self.shoelace(vertices, perimeter)

        pos = (0, 0)
        vertices = [pos]
        perimeter = 0
        for _, _, real_instruction in instructions:
            di, dj = self.real_dirs[real_instruction[-2:-1]]
            l = int("0x" + real_instruction[2:7], 16)
            pos = (pos[0] + di * l, pos[1] + dj * l)
            vertices.append(pos)
            perimeter += abs((di + dj) * l)

        result2 = self.shoelace(vertices, perimeter)

        return result1, result2


solver = Solution()
print(solver.solve("2023/q18.txt"))
