from collections import defaultdict


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        antennas = defaultdict(list)
        all_antennas = set()

        for i, line in enumerate(f.read().split("\n")):
            for j in range(len(line)):
                if line[j] != ".":
                    antennas[line[j]].append((i, j))
                    all_antennas.add((i, j))
        n, m = i + 1, j + 1

        # PART 1
        all_antinodes = set()
        for freq, locations in antennas.items():
            for i in range(1, len(locations)):
                for j in range(0, i):
                    x1, y1 = locations[i]
                    x2, y2 = locations[j]
                    dx, dy = x1 - x2, y1 - y2
                    if 0 <= x1 + dx < n and 0 <= y1 + dy < m:
                        all_antinodes.add((x1 + dx, y1 + dy))
                    if 0 <= x2 - dx < n and 0 <= y2 - dy < m:
                        all_antinodes.add((x2 - dx, y2 - dy))

        result1 = len(all_antinodes)

        # PART 2
        all_antinodes = set()
        for freq, locations in antennas.items():
            for i in range(1, len(locations)):
                for j in range(0, i):
                    x1, y1 = locations[i]
                    x2, y2 = locations[j]
                    dx = x1 - x2
                    dy = y1 - y2
                    while 0 <= x1 < n and 0 <= y1 < m:
                        all_antinodes.add((x1, y1))
                        x1, y1 = x1 + dx, y1 + dy
                    while 0 <= x2 < n and 0 <= y2 < m:
                        all_antinodes.add((x2, y2))
                        x2, y2 = x2 - dx, y2 - dy

        result2 = len(all_antinodes)

        return result1, result2


solver = Solution()
print(solver.solve("2024/q8.txt"))
