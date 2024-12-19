import heapq


class Solution:
    def __init__(self, debug=False):
        self.debug = debug

    def solve(self, filepath):
        result1, result2 = 10 ** 10, 0
        f = open(filepath, "r")
        _input = f.read().split("\n")

        valid_points = {}
        for i, line in enumerate(_input):
            for j, char in enumerate(list(line)):
                if char != "#":
                    valid_points[i + j * 1j] = char

        (start,) = (p for p in valid_points if valid_points[p] == "S")
        (end,) = (p for p in valid_points if valid_points[p] == "E")

        queue = [(0, 0, start, 1j, {start})]
        costs = {}
        seen = set()
        idx = 0
        max_size = 0

        while queue:
            cost, _, p, dir, path = heapq.heappop(queue)

            if cost > costs.get((p, dir), 10 ** 10):
                continue

            costs[(p, dir)] = cost

            if p == end and cost <= result1:
                seen |= path
                result1 = cost
                break

            for d, val in [(1, 1), (1j, 1001), (-1j, 1001)]:
                costp = cost + val
                pp = p + dir * d
                dirp = dir * d
                idx += 1
                if pp in valid_points and pp not in path:
                    heapq.heappush(queue, (costp, idx, pp, dirp, path | {pp}))

            max_size = max(max_size, len(queue))

        print(max_size, idx)
        result2 = len(seen)

        return result1, result2


solver = Solution()
print(solver.solve("2024/q16.txt"))
