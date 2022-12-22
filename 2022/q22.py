class Solution:
    def __init__(self):
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def get_graph_part1(self, grid):
        graph = dict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == ' ': continue
                graph[(i, j)] = dict()
                for di, dj in self.dirs:
                    k, l = (i + di)%len(grid), (j + dj)%len(grid[0])
                    while grid[k][l] == ' ':
                        k, l = (k + di)%len(grid), (l + dj)%len(grid[0])
                        if (k, l) == (i, j):
                            print(i, j, k, l, graph)
                            raise ValueError
                    if grid[k][l] == '.':
                        graph[(i, j)][(di, dj)] = (k, l)
                    else:
                        graph[(i, j)][(di, dj)] = (i, j)
        return graph

    def get_graph_part2(self, grid):
        def get_section(x, y):
            if 0 <= x < 50 and 100 <= y < 150: return 1
            elif 0 <= x < 50 and 50 <= y < 100: return 2
            elif 50 <= x < 100: return 3
            elif 100 <= x < 150 and 50 <= y < 100: return 4
            elif 100 <= x < 150 and 0 <= y < 50: return 5
            elif 150 <= x < 200: return 6
            return -1

        def get_offset(s):
            if s == 1: return (0, 100)
            elif s == 2: return (0, 50)
            elif s == 3: return (50, 50)
            elif s == 4: return (100, 50)
            elif s == 5: return (100, 0)
            elif s == 6: return (150, 0)

        
        def move(x, y, dx, dy):
            s = get_section(x, y)
            xo, yo = get_offset(s)
            xp, yp = (x + dx), (y + dy)
            if 50 <= xp+xo < 0 or 50 <= yp+yo < 0:
                a, b, c, d, e, f, (dx, dy) = neighbour[get_section(x,y)]
                xp, yp = a*xp+b*yp+c, d*xp+e*yp+f
            return xp, yp, dx, dy


        neighbour = {   1: {(0, 1):(-1, 0, 150, 0, 0, 99, (0, -1)), (1, 0):(-1, 0, 150, 0, 0, 99, (0, -1)), (0, -1):(1, 0, 0, 0, 1, 0, (0, -1)), (-1, 0):(-1, 0, 150, 0, 0, 99, (0, -1))},
                        2: {(0, 1):1, (1, 0):3, (0, -1):5, (-1, 0):6},
                        3: {(0, 1):1, (1, 0):4, (0, -1):5, (-1, 0):2},
                        4: {(0, 1):1, (1, 0):6, (0, -1):5, (-1, 0):3},
                        5: {(0, 1):4, (1, 0):6, (0, -1):2, (-1, 0):4},
                        6: {(0, 1):1, (1, 0):2, (0, -1):5, (-1, 0):4},
                    }

        graph = dict()
        n = 50
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == ' ': continue
                graph[(i, j)] = dict()
                for di, dj in self.dirs:
                    k, l, dl, dk = move(i, j, di, dj)
                    while grid[k][l] == ' ':
                        k, l = (k + di)%len(grid), (l + dj)%len(grid[0])
                        if (k, l) == (i, j):
                            print(i, j, k, l, graph)
                            raise ValueError
                    if grid[k][l] == '.':
                        graph[(i, j)][(di, dj)] = (k, l)
                    else:
                        graph[(i, j)][(di, dj)] = (i, j)
        return graph

    def get_instructions(self,codex):
        i = 0
        instructions = list()
        while i < len(codex):
            d = list()
            while i < len(codex) and codex[i].isnumeric():
                d.append(codex[i])
                i += 1
            if i < len(codex):
                instructions.append((int(''.join(d)), codex[i]))
            else:
                instructions.append((int(''.join(d)), 'Terminate'))
            i += 1
        return instructions

    def get_starting_position(self, graph):
        row, column, dir_idx = 0, 0, 0
        while not graph.get((row, column), None):
            column += 1
        return (row, column, dir_idx)

    def traverse(self, graph, instructions):
        row, column, dir_idx = self.get_starting_position(graph)
        for d, r in instructions:
            for i in range(d):
                row, column = graph[(row, column)][self.dirs[dir_idx]]
            if r == 'R': dir_idx = (dir_idx+1) % (len(self.dirs)) 
            elif r == 'L': dir_idx = (dir_idx-1) % (len(self.dirs))
        return row, column, dir_idx


    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        grid, codex = f.read().split("\n\n")
        grid = grid.split("\n")
        max_l = max([len(row) for row in grid])
        grid = [list(row.ljust(max_l)) for row in grid]
        # print(codex)
        print(len(grid), len(grid[0]))
        
        graph = self.get_graph_part1(grid)
        instructions = self.get_instructions(codex)
        row, column, dir_idx = self.traverse(graph, instructions)
        
        result1 = (row+1)*1000 + (column+1)*4 + dir_idx


        graph = self.get_graph_part2(grid)
        row, column, dir_idx = self.traverse(graph, instructions)
            

        return result1, result2


solver = Solution()
print(solver.solve("2022/q22.txt"))
