class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, 'r')
        result, result2 = 0, 1
        grid = list()
        
        for line in f.readlines():
            x = line.strip('\n')
            row = list()
            for c in x:
                if c == '.': row.append(0)
                else: row.append(1)
            grid.append(row)
        
        i, j = 1, 3
        while i < len(grid):
            if grid[i][j%len(grid[i])] == 1:
                result += 1
            i += 1
            j += 3
        
        deltas = [(1,1), (1,3), (1,5), (1,7), (2,1)]
        for di, dj in deltas:
            i, j, temp = di, dj, 0
            while i < len(grid):
                if grid[i][j%len(grid[i])] == 1:
                    temp += 1
                i += di
                j += dj
            result2 *= temp
            
        return result, result2 

solver = Solution()
print(solver.solve('2020/q3.txt'))
