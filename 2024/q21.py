from functools import lru_cache


class Solution:
    def __init__(self):
        self.numpad = ["789", "456", "123", " 0A"]
        self.contpad = [" ^A", "<v>"]

    def get_coordinates(self, depth, char):
        grid = self.contpad if depth != 0 else self.numpad
        return next(
            (x, y) for y, r in enumerate(grid) for x, c in enumerate(r) if c == char
        )

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        keystrokes = {line: int(line[:3]) for line in f.read().split("\n")}
        print(keystrokes)

        def search(curr: str, next_: str, depth: int):
            grid = self.contpad if depth != 0 else self.numpad
            fx, fy = self.get_coordinates(depth, curr)
            tx, ty = self.get_coordinates(depth, next_)

            queue = [(fx, fy, "")]
            results = []
            while queue:
                x, y, s = queue.pop(0)
                if (x, y) == (tx, ty):
                    results.append(s + "A")
                if tx < x and grid[y][x - 1] != " ":
                    queue.append((x - 1, y, s + "<"))
                if ty < y and grid[y - 1][x] != " ":
                    queue.append((x, y - 1, s + "^"))
                if ty > y and grid[y + 1][x] != " ":
                    queue.append((x, y + 1, s + "v"))
                if tx > x and grid[y][x + 1] != " ":
                    queue.append((x + 1, y, s + ">"))

            # Prefer paths with least change
            return min(
                results,
                key=lambda path: sum(
                    path[i - 1] != path[i] for i in range(1, len(path))
                ),
            )

        @lru_cache
        def parse(keystroke: str, depth: int = 0, max_depth: int = 2):
            result = 0
            if depth > max_depth:
                return len(keystroke)

            for curr, next_ in zip("A" + keystroke, keystroke):
                result += parse(
                    keystroke=search(curr, next_, depth),
                    depth=depth + 1,
                    max_depth=max_depth,
                )

            return result

        # PART 1
        for ks, mul in keystrokes.items():
            result1 += parse(ks) * mul

        # PART 2
        for ks, mul in keystrokes.items():
            result2 += parse(ks, max_depth=25) * mul

        return result1, result2


solver = Solution()
print(solver.solve("2024/q21.txt"))
