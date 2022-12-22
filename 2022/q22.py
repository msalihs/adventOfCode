class Solution:
    def __init__(self):
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def get_graph_part1(self, grid):
        graph = dict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == " ":
                    continue
                graph[(i, j)] = dict()
                for di, dj in self.dirs:
                    k, l = (i + di) % len(grid), (j + dj) % len(grid[0])
                    while grid[k][l] == " ":
                        k, l = (k + di) % len(grid), (l + dj) % len(grid[0])
                        if (k, l) == (i, j):
                            print(i, j, k, l, graph)
                            raise ValueError
                    if grid[k][l] == ".":
                        graph[(i, j)][(di, dj)] = (k, l, di, dj)
                    else:
                        graph[(i, j)][(di, dj)] = (i, j, di, dj)
        return graph

    def get_graph_part2(self, grid):
        def get_section(x, y):
            if 0 <= x < 50 and 100 <= y < 150:
                return 1
            elif 0 <= x < 50 and 50 <= y < 100:
                return 2
            elif 50 <= x < 100:
                return 3
            elif 100 <= x < 150 and 50 <= y < 100:
                return 4
            elif 100 <= x < 150 and 0 <= y < 50:
                return 5
            elif 150 <= x < 200:
                return 6
            return -1

        def move(x, y, dx, dy):
            s = get_section(x, y)
            xo, yo = offsets[s]
            xp, yp = (x + dx), (y + dy)
            dxp, dyp = dx, dy
            if 50 <= xp - xo or xp - xo < 0 or 50 <= yp - yo or yp - yo < 0:
                a, b, c, d, e, f, (dxp, dyp) = neighbour[s][(dx, dy)]
                xp, yp = a * xp + b * yp + c, d * xp + e * yp + f
            return xp, yp, dxp, dyp

        offsets = {
            1: (0, 100),
            2: (0, 50),
            3: (50, 50),
            4: (100, 50),
            5: (100, 0),
            6: (150, 0),
        }

        neighbour = {
            1: {
                (0, 1): (-1, 0, 149, 0, 0, 99, (0, -1)),
                (1, 0): (0, 1, -50, 0, 0, 99, (0, -1)),
                (0, -1): (1, 0, 0, 0, 1, 0, (0, -1)),
                (-1, 0): (0, 0, 199, 0, 1, -100, (-1, 0)),
            },
            2: {
                (0, 1): (1, 0, 0, 0, 1, 0, (0, 1)),
                (1, 0): (1, 0, 0, 0, 1, 0, (1, 0)),
                (-1, 0): (0, 1, 100, 0, 0, 0, (0, 1)),
                (0, -1): (-1, 0, 149, 0, 0, 0, (0, 1)),
            },
            3: {
                (0, -1): (0, 0, 100, 1, 0, -50, (1, 0)),
                (0, 1): (0, 0, 49, 1, 0, 50, (-1, 0)),
                (1, 0): (1, 0, 0, 0, 1, 0, (1, 0)),
                (-1, 0): (1, 0, 0, 0, 1, 0, (-1, 0)),
            },
            4: {
                (1, 0): (0, 1, 100, 0, 0, 49, (0, -1)),
                (-1, 0): (1, 0, 0, 0, 1, 0, (-1, 0)),
                (0, -1): (1, 0, 0, 0, 1, 0, (0, -1)),
                (0, 1): (-1, 0, 149, 0, 0, 149, (0, -1)),
            },
            5: {
                (0, 1): (1, 0, 0, 0, 1, 0, (0, 1)),
                (1, 0): (1, 0, 0, 0, 1, 0, (1, 0)),
                (-1, 0): (0, 1, 50, 0, 0, 50, (0, 1)),
                (0, -1): (-1, 0, 149, 0, 0, 50, (0, 1)),
            },
            6: {
                (-1, 0): (1, 0, 0, 0, 1, 0, (-1, 0)),
                (1, 0): (0, 0, 0, 0, 1, 100, (1, 0)),
                (0, -1): (0, 0, 0, 1, 0, -100, (1, 0)),
                (0, 1): (0, 0, 149, 1, 0, -100, (-1, 0)),
            },
        }

        graph = dict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == " ":
                    continue
                graph[(i, j)] = dict()
                for di, dj in self.dirs:
                    k, l, dl, dk = move(i, j, di, dj)
                    if grid[k][l] == ".":
                        graph[(i, j)][(di, dj)] = (k, l, dl, dk)
                    else:
                        graph[(i, j)][(di, dj)] = (i, j, di, dj)
        return graph

    def get_instructions(self, codex):
        i = 0
        instructions = list()
        while i < len(codex):
            d = list()
            while i < len(codex) and codex[i].isnumeric():
                d.append(codex[i])
                i += 1
            if i < len(codex):
                instructions.append((int("".join(d)), codex[i]))
            else:
                instructions.append((int("".join(d)), "Terminate"))
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
                row, column, di, dj = graph[(row, column)][self.dirs[dir_idx]]
                dir_idx = self.dirs.index((di, dj))
            if r == "R":
                dir_idx = (dir_idx + 1) % (len(self.dirs))
            elif r == "L":
                dir_idx = (dir_idx - 1) % (len(self.dirs))
        return row, column, dir_idx

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        grid, codex = f.read().split("\n\n")
        grid = grid.split("\n")
        max_l = max([len(row) for row in grid])
        grid = [list(row.ljust(max_l)) for row in grid]

        graph = self.get_graph_part1(grid)
        instructions = self.get_instructions(codex)
        row, column, dir_idx = self.traverse(graph, instructions)
        result1 = (row + 1) * 1000 + (column + 1) * 4 + dir_idx

        graph = self.get_graph_part2(grid)
        row, column, dir_idx = self.traverse(graph, instructions)
        result2 = (row + 1) * 1000 + (column + 1) * 4 + dir_idx

        return result1, result2


solver = Solution()
print(solver.solve("2022/q22.txt"))
