from collections import defaultdict, deque
import time


class Solution:
    def __init__(self, filepath):
        f = open(filepath, "r")
        self.rock_shapes = [
            [list("####")],
            [list(".#."), list("###"), list(".#.")],
            [list("..#"), list("..#"), list("###")],
            [list("#"), list("#"), list("#"), list("#")],
            [list("##"), list("##")],
        ]
        self.movements = list(f.read())
        self.stack = deque([list("#########")])
        self.wind_idx = 0
        self.last_element = 1
        self.rock_idx = 0

    def reset(self):
        self.stack = deque([list("#########")])
        self.wind_idx = 0
        self.rock_idx = 0
        self.last_element = 1

    def apply_wind(self, r, x, h):
        dir = self.movements[self.wind_idx % len(self.movements)]
        if dir == ">" and self.can_move_right(r, x, h):
            x += 1
        if dir == "<" and self.can_move_left(r, x, h):
            x -= 1
        self.wind_idx += 1
        return x

    def can_move_right(self, r, x, h):
        if len(r[0]) + x + 2 > len(self.stack[0]):
            return False
        else:
            for i in range(min(h, len(r))):
                for j in reversed(range(len(r[0]))):
                    if r[-1 - i][j] == "#" and self.stack[h - i][x + j + 1] == "#":
                        return False
        return True

    def can_move_left(self, r, x, h):
        if x < 2:
            return False
        else:
            for i in range(min(h, len(r))):
                for j in range(len(r[0])):
                    if r[-1 - i][j] == "#" and self.stack[h - i][x + j - 1] == "#":
                        return False
        return True

    def can_move_down(self, r, x, h):
        if h < 3:
            return True
        for i in range(len(r)):
            for j in range(len(r[0])):
                if r[-1 - i][j] == "#" == self.stack[h - i][x + j]:
                    return False
        return True

    def new_row(self):
        if len(self.stack) > 500:
            self.stack.pop()
        self.stack.appendleft(list("#.......#"))
        self.last_element += 1

    def drop_n_rocks(self, n):
        for i in range(n):
            for j in range(3):
                if self.stack[j] != list("#.......#"):
                    self.new_row()

            rock = self.rock_shapes[self.rock_idx % len(self.rock_shapes)]
            self.rock_idx += 1
            x, h, l = 3, -1, len(rock) - 1
            x = self.apply_wind(rock, x, h)
            while self.can_move_down(rock, x, h + 1):
                h += 1
                x = self.apply_wind(rock, x, h)

            while h >= 0 and l >= 0:
                for i in range(len(rock[0])):
                    if self.stack[h][x + i] != "#":
                        self.stack[h][x + i] = rock[l][i]
                h, l = h - 1, l - 1

            while l >= 0:
                self.new_row()
                for i in range(len(rock[0])):
                    self.stack[0][x + i] = rock[l][i]
                l -= 1

        while self.stack[0] == list("#.......#"):
            self.last_element -= 1
            self.stack.popleft()

        return self.last_element - 1

    def get_stack_hash(self):
        return sum([hash("".join(s)) for s in self.stack])

    def solve(self):
        result1, result2 = 0, 0
        s = time.time()
        result1 = self.drop_n_rocks(n=2022)
        print(f"It took {time.time()-s} seconds")
        self.reset()

        cache = defaultdict(dict)
        i = 0
        t = 1000000000000
        while i < t:
            h = self.drop_n_rocks(n=1)
            shash = self.get_stack_hash()
            idx = self.wind_idx % len(self.movements)
            if shash in cache[idx]:
                prev_h, prev_i = cache[idx][shash]
                h_diff = h - prev_h
                i_diff = i - prev_i
                d, m = divmod((t - i - 1), i_diff)
                self.last_element += h_diff * d
                i += i_diff * d
            cache[idx][shash] = (h, i)
            i += 1

        result2 = self.last_element - 1

        return result1, result2


solver = Solution("2022/q17.txt")
print(solver.solve())
