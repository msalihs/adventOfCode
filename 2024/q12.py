import itertools


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        grid = [line.strip() for line in f.readlines()]

        n, m = len(grid), len(grid[0])
        seen = set()

        def get_area_and_perimeter(i, j, count_sides=False):
            val = grid[i][j]
            queue = [(i, j)]
            area = set()
            perimeter = dict()
            corners = 0

            while queue:
                i, j = queue.pop()
                area.add((i, j))
                for di, dj in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                    ip, jp = i + di, j + dj
                    if 0 <= ip < n and 0 <= jp < m and grid[ip][jp] == val:
                        if (ip, jp) not in seen:
                            queue.append((ip, jp))
                            seen.add((ip, jp))
                    else:
                        perimeter[(ip, jp)] = perimeter.get((ip, jp), 0) + 1

            if count_sides:
                for i, j in area:
                    for di, dj in itertools.product([-1, 1], repeat=2):
                        if {(i + di, j), (i, j + dj)}.issubset(perimeter):
                            corners += 1
                for i, j in perimeter.keys():
                    for di, dj in itertools.product([-1, 1], repeat=2):
                        if {(i + di, j), (i, j + dj), (i + di, j + dj)}.issubset(area):
                            corners += 1

            return len(area), corners if count_sides else sum(perimeter.values())

        # PART 1
        for i in range(n):
            for j in range(m):
                if (i, j) not in seen:
                    seen.add((i, j))
                    area, perimeter = get_area_and_perimeter(i, j)
                    result1 += area * perimeter

        # PART 2
        seen = set()
        for i in range(n):
            for j in range(m):
                if (i, j) not in seen:
                    seen.add((i, j))
                    area, perimeter = get_area_and_perimeter(i, j, count_sides=True)
                    result2 += area * perimeter

        return result1, result2


solver = Solution()
print(solver.solve("2024/q12.txt"))
