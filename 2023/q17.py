import heapq


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 10 ** 9, 0
        grid = [[int(c) for c in row] for row in f.read().split("\n") if row]

        # queue = [(grid[0][1], 0, 1, 0, 1), (grid[1][0], 1, 0, 1, 0)]
        # seen = {(1,0):grid[1][0], (0,1):grid[0][1]}
        # dest = (len(grid)-1, len(grid[0])-1)
        # max_straight = 3
        # while queue:
        #     # print(queue)
        #     heat, i, j, di, dj = heapq.heappop(queue)
        #     if (i, j) == dest:
        #         result1 = heat
        #     # Moving down
        #     if di > 0:
        #         if 0 <= j - 1 and seen.get((i, j-1, 0, -1), 10**9) > (heat + grid[i][j-1]):
        #             heapq.heappush(queue,(heat + grid[i][j-1], i, j-1, 0, -1))
        #             seen[(i, j-1, 0, -1)] = heat + grid[i][j-1]
        #         if (j+1) < len(grid[0]) and seen.get((i, j+1, 0, 1), 10**9) > (heat + grid[i][j+1]):
        #             heapq.heappush(queue,(heat + grid[i][j+1], i, j+1, 0, 1))
        #             seen[(i, j+1, 0, 1)] = heat + grid[i][j+1]
        #         if di < max_straight and (i+1) < len(grid) and seen.get((i+1, j, di+1, 0), 10**9) > (heat + grid[i+1][j]):
        #             heapq.heappush(queue,(heat + grid[i+1][j], i+1, j, di+1, 0))
        #             seen[(i+1, j, di+1, 0)] = heat + grid[i+1][j]
        #     # Moving up
        #     if di < 0:
        #         if 0 <= j - 1 and seen.get((i, j-1, 0, -1), 10**9) > (heat + grid[i][j-1]):
        #             heapq.heappush(queue,(heat + grid[i][j-1], i, j-1, 0, -1))
        #             seen[(i, j-1, 0, -1)] = heat + grid[i][j-1]
        #         if (j+1) < len(grid[0]) and seen.get((i, j+1, 0, 1), 10**9) > (heat + grid[i][j+1]):
        #             heapq.heappush(queue,(heat + grid[i][j+1], i, j+1, 0, 1))
        #             seen[(i, j+1, 0, 1)] = heat + grid[i][j+1]
        #         if di > -max_straight and 0 <= (i-1) and seen.get((i-1, j, di-1, 0), 10**9) > (heat + grid[i-1][j]):
        #             heapq.heappush(queue,(heat + grid[i-1][j], i-1, j, di-1, 0))
        #             seen[(i-1, j, di-1, 0)] = heat + grid[i-1][j]
        #     # Moving left
        #     if dj < 0:
        #         if 0 <= i-1 and seen.get((i-1, j, -1, 0), 10**9) > (heat + grid[i-1][j]):
        #             heapq.heappush(queue,(heat + grid[i-1][j], i-1, j, -1, 0))
        #             seen[(i-1, j, -1, 0)] = heat + grid[i-1][j]
        #         if (i+1) < len(grid) and seen.get((i+1, j, 1, 0), 10**9) > (heat + grid[i+1][j]):
        #             heapq.heappush(queue,(heat + grid[i+1][j], i+1, j, 1, 0))
        #             seen[(i+1, j, 1, 0)] = heat + grid[i+1][j]
        #         if dj > -max_straight and 0 <= (j-1) and seen.get((i, j-1, 0, dj-1), 10**9) > (heat + grid[i][j-1]):
        #             heapq.heappush(queue,(heat + grid[i][j-1], i, j-1, 0, dj-1))
        #             seen[(i, j-1, 0, dj-1)] = heat + grid[i][j-1]
        #     # Moving right
        #     if dj > 0:
        #         if 0 <= i-1 and seen.get((i-1, j, -1, 0), 10**9) > (heat + grid[i-1][j]):
        #             heapq.heappush(queue,(heat + grid[i-1][j], i-1, j, -1, 0))
        #             seen[(i-1, j, -1, 0)] = heat + grid[i-1][j]
        #         if (i+1) < len(grid) and seen.get((i+1, j, 1, 0), 10**9) > (heat + grid[i+1][j]):
        #             heapq.heappush(queue,(heat + grid[i+1][j], i+1, j, 1, 0))
        #             seen[(i+1, j, 1, 0)] = heat + grid[i+1][j]
        #         if dj < max_straight and (j+1) < len(grid[0]) and seen.get((i, j+1, 0, dj+1), 10**9) > (heat + grid[i][j+1]):
        #             heapq.heappush(queue,(heat + grid[i][j+1], i, j+1, 0, dj+1))
        #             seen[(i, j+1, 0, dj+1)] = heat + grid[i][j+1]
        # print(len(seen))

        queue = [(0, 0, 1, 0, 1), (0, 0, 1, 1, 0)]
        dest = (len(grid) - 1, len(grid[0]) - 1)
        max_straight = 3
        seen = set()
        while queue:
            # print(queue)
            heat, i, j, di, dj = heapq.heappop(queue)
            if (i, j, di, dj) in seen:
                continue
            seen.add((i, j, di, dj))
            if (i, j) == dest:
                result1 = min(heat, result1)
            # Moving down
            if di > 0:
                if 0 <= j - 1:
                    heapq.heappush(queue, (heat + grid[i][j - 1], i, j - 1, 0, -1))
                if (j + 1) < len(grid[0]):
                    heapq.heappush(queue, (heat + grid[i][j + 1], i, j + 1, 0, 1))
                if di < max_straight and (i + 1) < len(grid):
                    heapq.heappush(queue, (heat + grid[i + 1][j], i + 1, j, di + 1, 0))
            # Moving up
            if di < 0:
                if 0 <= j - 1:
                    heapq.heappush(queue, (heat + grid[i][j - 1], i, j - 1, 0, -1))
                if (j + 1) < len(grid[0]):
                    heapq.heappush(queue, (heat + grid[i][j + 1], i, j + 1, 0, 1))
                if di > -max_straight and 0 <= (i - 1):
                    heapq.heappush(queue, (heat + grid[i - 1][j], i - 1, j, di - 1, 0))
            # Moving left
            if dj < 0:
                if 0 <= i - 1:
                    heapq.heappush(queue, (heat + grid[i - 1][j], i - 1, j, -1, 0))
                if (i + 1) < len(grid):
                    heapq.heappush(queue, (heat + grid[i + 1][j], i + 1, j, 1, 0))
                if dj > -max_straight:
                    heapq.heappush(queue, (heat + grid[i][j - 1], i, j - 1, 0, dj - 1))
            # Moving right
            if dj > 0:
                if 0 <= i - 1:
                    heapq.heappush(queue, (heat + grid[i - 1][j], i - 1, j, -1, 0))
                if (i + 1) < len(grid):
                    heapq.heappush(queue, (heat + grid[i + 1][j], i + 1, j, 1, 0))
                if dj < max_straight and (j + 1) < len(grid[0]):
                    heapq.heappush(queue, (heat + grid[i][j + 1], i, j + 1, 0, dj + 1))

        return result1, result2


solver = Solution()
print(solver.solve("2023/q17.txt"))
