from collections import deque
import heapq


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        bricks = [
            [tuple(int(c) for c in r.split(",")) for r in reading.split("~")]
            for reading in f.read().split("\n")
        ]
        # print(bricks)
        queue = list()
        maxz, maxx, maxy = 0, 0, 0
        for idx, (p1, p2) in enumerate(bricks):
            minz = min(p1[2], p2[2])
            heapq.heappush(queue, (minz, idx + 1, p1, p2))
            maxx = max(p1[0], p2[0], maxx)
            maxy = max(p1[1], p2[1], maxy)
            maxz = max(p1[2], p2[2], maxz)

        grid = {i: [[0] * (maxx + 1) for _ in range(maxy + 1)] for i in range(maxz)}
        graph = dict()
        while queue:
            minz, idx, p1, p2 = heapq.heappop(queue)
            graph[idx] = set()
            zpos = maxz - 1
            while len(graph[idx]) == 0 and zpos > 0:
                for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                    for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                        if grid[zpos][y][x] != 0:
                            graph[idx].add(grid[zpos][y][x])
                if len(graph[idx]) == 0:
                    zpos -= 1
            zpos += 1
            for z in range(max(p1[2], p2[2]) - min(p1[2], p2[2]) + 1):
                for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                    for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                        grid[zpos + z][y][x] = idx

        reverse_graph = dict()
        for idx, nei in graph.items():
            for nei_idx in nei:
                if nei_idx in reverse_graph:
                    reverse_graph[nei_idx].add(idx)
                else:
                    reverse_graph[nei_idx] = {idx}

        disintegratable = set(range(1, len(bricks) + 1))
        for v in graph.values():
            if len(v) == 1:
                disintegratable.discard(list(v)[0])
        result1 = len(disintegratable)

        others = set(range(1, len(bricks) + 1)) - disintegratable
        result2 = 0
        for k in others:
            queue, seen = deque([k]), {k}
            while queue:
                idx = queue.popleft()
                for nei in reverse_graph.get(idx, set()):
                    if nei not in seen and seen.issuperset(graph[nei]):
                        queue.append(nei)
                        seen.add(nei)
                        result2 += 1
        return result1, result2


solver = Solution()
print(solver.solve("2023/q22.txt"))
