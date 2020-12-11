class Solution:
    def __init__(self):
        pass

    def same(self, m1, m2):
        for i in len(m1):
            for j in len(m1[0]):
                if m1[i][j] != m2[i][j]: return False
        return True

    def solve(self, filepath):
        f = open(filepath, 'r')
        result1, result2 = 0, 0
        grid = list()

        for line in f.readlines():
            t = list()
            for c in line:
                if c == '.': t.append(0)
                elif c == 'L': t.append(1)
            grid.append(t)
        n, m = len(grid), len(grid[0])
        originalGrid = grid[:][:]

        # PART 1
        while True:
            newGrid = list()
            for i in range(n):
                t = list()
                for j in range(m):

                    adjOccupied = 0
                    for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                        if 0 <= i + di < n and 0 <= j + dj < m:
                            if grid[i + di][j + dj] == 2: 
                                adjOccupied += 1

                    if grid[i][j] == 1 and adjOccupied == 0:
                        t.append(2)
                    elif grid[i][j] == 2 and adjOccupied > 3:
                        t.append(1)
                    else:
                        t.append(grid[i][j])
                
                newGrid.append(t)

            if newGrid == grid:
                print(grid[0])
                result1 = sum([1 for row in newGrid for x in row  if x == 2])
                break
            grid = newGrid[:][:]

        # PART 2
        grid = originalGrid[:][:]
        while True:
            newGrid = list()
            for i in range(n):
                t = list()
                for j in range(m):

                    adjOccupied = 0
                    for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                        k = 1
                        while 0 <= i + (k*di) < n and 0 <= j + (k*dj) < m:
                            if grid[i + (k*di)][j + (k*dj)] != 0:
                                if grid[i + (k*di)][j + (k*dj)] == 2: adjOccupied += 1
                                break
                            else: k += 1

                    if grid[i][j] == 1 and adjOccupied == 0:
                        t.append(2)
                    elif grid[i][j] == 2 and adjOccupied > 4:
                        t.append(1)
                    else:
                        t.append(grid[i][j])
                
                newGrid.append(t)

            if newGrid == grid:
                print(grid[0])
                result2 = sum([1 for row in newGrid for x in row  if x == 2])
                break
            grid = newGrid[:][:]

        return result1, result2

solver = Solution()
print(solver.solve('2020/q11.txt'))
