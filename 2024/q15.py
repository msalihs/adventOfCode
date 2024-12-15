class Solution:
    def __init__(self, debug=False):
        self.debug = debug

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        grid_input, moves = f.read().split("\n\n")
        moves = [c for move in moves.split("\n") for c in move.strip()]
        delta = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

        def can_move(i, j, di, dj):
            if grid[i + di][j + dj] == ".":
                return True
            elif grid[i + di][j + dj] == "O":
                return can_move(i + di, j + dj, di, dj)
            elif di != 0 and grid[i + di][j + dj] == "[":
                r1 = can_move(i + di, j + dj, di, dj)
                r2 = can_move(i + di, j + dj + 1, di, dj)
                return r1 and r2
            elif di != 0 and grid[i + di][j + dj] == "]":
                r1 = can_move(i + di, j + dj, di, dj)
                r2 = can_move(i + di, j + dj - 1, di, dj)
                return r1 and r2
            elif di == 0 and grid[i + di][j + dj] == "]":
                return can_move(i + di, j + dj - 1, di, dj)
            elif di == 0 and grid[i + di][j + dj] == "[":
                return can_move(i + di, j + dj + 1, di, dj)
            return False

        def swap(i, j, di, dj):
            if grid[i + di][j + dj] == "O":
                swap(i + di, j + dj, di, dj)
            elif di != 0 and grid[i + di][j + dj] == "[":
                swap(i + di, j + dj, di, dj)
                swap(i + di, j + dj + 1, di, dj)
            elif di != 0 and grid[i + di][j + dj] == "]":
                swap(i + di, j + dj, di, dj)
                swap(i + di, j + dj - 1, di, dj)
            elif di == 0 and grid[i + di][j + dj] == "]":
                swap(i + di, j + dj - 1, di, dj)
                swap(i + di, j + dj, di, dj)
            elif di == 0 and grid[i + di][j + dj] == "[":
                swap(i + di, j + dj + 1, di, dj)
                swap(i + di, j + dj, di, dj)
            if grid[i + di][j + dj] == ".":
                grid[i + di][j + dj], grid[i][j] = grid[i][j], grid[i + di][j + dj]

        def get_start_position(grid):
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == "@":
                        return i, j

        def get_final_score(grid):
            result = 0
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] in {"[", "O"}:
                        result += i * 100 + j
            return result

        # PART 1
        grid = [list(c.strip()) for c in grid_input.split("\n")]
        i, j = get_start_position(grid)

        for idx, move in enumerate(moves):
            di, dj = delta[move]
            if can_move(i, j, di, dj):
                swap(i, j, di, dj)
                i += di
                j += dj

        result1 = get_final_score(grid)

        # PART 2
        grid = [list(c.strip()) for c in grid_input.split("\n")]
        new_grid = list()
        mapping = {"#": "##", ".": "..", "O": "[]", "@": "@."}
        for i in range(len(grid)):
            new_grid.append(list())
            for j in range(len(grid[i])):
                new_grid[i] += list(mapping[grid[i][j]])

        grid = new_grid
        i, j = get_start_position(grid)

        for idx, move in enumerate(moves):
            di, dj = delta[move]
            if can_move(i, j, di, dj):
                swap(i, j, di, dj)
                i += di
                j += dj

            if self.debug:
                with open("output.txt", "a") as output_file:
                    output_file.write(f"----ITERATION {idx} {move} {delta[move]}----")
                    output_file.write("\n".join(["".join(row) for row in grid]) + "\n")
                    output_file.write("-------------------\n")

        result2 = get_final_score(grid)

        return result1, result2


solver = Solution()
print(solver.solve("2024/q15.txt"))
