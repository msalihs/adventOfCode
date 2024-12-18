import heapq


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        coords = [tuple([int(x) for x in c.split(",")]) for c in f.read().split("\n")]
        n = max([max(x + 1, y + 1) for x, y in coords])
        dt = 1024

        for t in [dt] + list(reversed(range(len(coords)))):
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

            if t == dt:
                result1 = result
            elif result == 0:
                result2 = coords[t - 1]
            else:
                break

        return result1, result2


solver = Solution()
print(solver.solve("2024/q18.txt"))
