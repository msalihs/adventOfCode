import heapq


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        grid = [[int(c) for c in row] for row in f.read().split("\n") if row]
        start = (0, 0, 0, 1, 1)
        queue = [start]
        seen = {(0, 0, 1, 1)}
        dest = (len(grid) - 1, len(grid[0]) - 1)

        def helper_add_to_queue(new_node, max_d, add_cost=True):
            cost, i, j, di, dj = new_node
            if (
                abs(di) <= (max_d)
                and abs(dj) <= (max_d)
                and (i, j, di, dj) not in seen
                and 0 <= i < len(grid)
                and 0 <= j < len(grid[0])
            ):
                if add_cost:
                    cost += grid[i][j]
                heapq.heappush(queue, (cost, i, j, di, dj))
                seen.add((i, j, di, dj))

        while queue:
            cost, i, j, di, dj = heapq.heappop(queue)
            if (i, j) == dest:
                result1 = cost
                break
            if di != 0:
                delta = 1 if di > 0 else -1
                helper_add_to_queue((cost, i + delta, j, di + delta, 0), 3)
                helper_add_to_queue((cost, i, j + 1, 0, 1), 3)
                helper_add_to_queue((cost, i, j - 1, 0, -1), 3)
            if dj != 0:
                delta = 1 if dj > 0 else -1
                helper_add_to_queue((cost, i, j + delta, 0, dj + delta), 3)
                helper_add_to_queue((cost, i + 1, j, 1, 0), 3)
                helper_add_to_queue((cost, i - 1, j, -1, 0), 3)

        start = (0, 0, 0, 1, 1)
        queue = [start]
        seen = {(0, 0, 1, 1)}
        while queue:
            cost, i, j, di, dj = heapq.heappop(queue)
            if (i, j) == dest:
                print(cost, i, j, di, dj)
                result2 = cost
                break
            if di != 0:
                delta = 1 if di > 0 else -1
                if (cost, i, j, di, dj) != start:
                    helper_add_to_queue((cost, i + delta, j, di + delta, 0), 10)
                costp = cost + sum(
                    [grid[i][jp] for jp in range(j + 1, j + 5) if jp < len(grid[0])]
                )
                helper_add_to_queue((costp, i, j + 4, 0, 4), 10, False)
                costp = cost + sum([grid[i][jp] for jp in range(j - 4, j) if 0 <= jp])
                helper_add_to_queue((costp, i, j - 4, 0, -4), 10, False)
            if dj != 0:
                delta = 1 if dj > 0 else -1
                if (cost, i, j, di, dj) != start:
                    helper_add_to_queue((cost, i, j + delta, 0, dj + delta), 10)
                costp = cost + sum(
                    [grid[ip][j] for ip in range(i + 1, i + 5) if ip < len(grid)]
                )
                helper_add_to_queue((costp, i + 4, j, 4, 0), 10, False)
                costp = cost + sum([grid[ip][j] for ip in range(i - 4, i) if 0 <= ip])
                helper_add_to_queue((costp, i - 4, j, -4, 0), 10, False)
        return result1, result2


solver = Solution()
print(solver.solve("2023/q17.txt"))
