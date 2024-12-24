class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        _input = f.read().split("\n")

        path = {}
        for i, line in enumerate(_input):
            for j, char in enumerate(list(line)):
                if char != "#":
                    path[i + j * 1j] = char

        (start,) = (p for p in path if path[p] == "S")
        (end,) = (p for p in path if path[p] == "E")

        distances = {start: 0}
        queue = [start]

        while queue and end not in queue:
            node = queue.pop()
            for delta in [-1, +1, -1j, +1j]:
                nei = node + delta
                if nei in path and nei not in distances:
                    distances[nei] = distances[node] + 1
                    queue.append(nei)

        def get_distance(p1: complex, p2: complex):
            return abs((p1 - p2).real) + abs((p1 - p2).imag)

        print(len(distances))

        for p1 in distances:
            for p2 in distances:
                if distances[p2] > distances[p1]:
                    dist = get_distance(p1, p2)
                    saved_dist = distances[p2] - distances[p1] - dist
                    if dist == 2 and saved_dist >= 100:
                        result1 += 1
                    if dist < 21 and saved_dist >= 100:
                        result2 += 1

        return result1, result2


solver = Solution()
print(solver.solve("2024/q20.txt"))
