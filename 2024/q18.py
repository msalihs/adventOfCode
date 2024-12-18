import heapq


class Solution:
    def __init__(self, debug=False):
        self.debug = debug

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        coords = [tuple([int(x) for x in c.split(",")]) for c in f.read().split("\n")]
        n = 71
        t = 1024

        for t in [1024] + list(reversed(range(len(coords)))):
            queue = [(0, 0, 0)]
            seen = set((0, 0)) | set(coords[:t])
            target = (n - 1, n - 1)
            result = 0

            while queue and result == 0:
                l, i, j = heapq.heappop(queue)
                for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    ip, jp = i + di, j + dj
                    if 0 <= ip < n and 0 <= jp < n and (ip, jp) not in seen:
                        heapq.heappush(queue, (l + 1, ip, jp))
                        seen.add((ip, jp))
                    if (ip, jp) == target:
                        result = l + 1

            if t == 1024:
                result1 = result
            elif result > 0:
                result2 = t + 1
                break

        return result1, result2


solver = Solution()
print(solver.solve("2024/q18.txt"))
