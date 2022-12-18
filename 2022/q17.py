from collections import deque


class Solution:
    def __init__(self, filepath):
        f = open(filepath, "r")
        self.rock_shapes = [[list('####')], [list('.#.'), list('###'),list('.#.')], [list('..#'), list('..#'), list('###')], [list('#'), list('#'), list('#'), list('#')], [list('##'), list('##')]]
        # self.rock_shapes = [[list('.#.'), list('###'),list('.#.')], [list('#'), list('#'), list('#'), list('#')]]
        self.movements = list(f.read())
        self.stack = deque([list('#########')])
        self.wind_idx = 0
        self.last_element = 1
        print(len(self.movements))

    def apply_wind(self, r, x, h):
        dir = self.movements[self.wind_idx % len(self.movements)]
        if dir == '>' and self.can_move_right(r, x, h):
            x += 1
        if dir == '<' and self.can_move_left(r, x, h):
            x -= 1
        self.wind_idx += 1
        return x

    def can_move_right(self, r, x, h):
        if len(r[0]) + x + 2 > len(self.stack[0]):
            return False
        else:
            for i in range(min(h, len(r))):
                for j in reversed(range(len(r[0]))):
                    if r[-1-i][j] == '#' and self.stack[h-i][x+j+1] == '#':
                        return False
        return True

        
    def can_move_left(self, r, x, h):
        if x < 2:
            return False
        else:
            for i in range(min(h, len(r))):
                for j in range(len(r[0])):
                    if r[-1-i][j] == '#' and self.stack[h-i][x+j-1] == '#':
                        return False
        return True

        
    def can_move_down(self, r, x, h):
        if h < 3:
            return True
        for i in range(len(r)):
            for j in range(len(r[0])):
                if r[-1-i][j] == '#' == self.stack[h-i][x+j]:
                    return False
        return True

    def solve(self):
        result1, result2 = 0, 0

        for i in range(2022):
            for _ in range(3 - len(self.stack) + self.last_element):
                self.stack.appendleft(list('#.......#'))
            rock = self.rock_shapes[i % len(self.rock_shapes)]
            x, h, l = 3, -1, len(rock) - 1
            x = self.apply_wind(rock, x, h)
            while self.can_move_down(rock, x, h+1):
                h += 1
                x = self.apply_wind(rock, x, h)

            while h >= 0 and l >= 0:
                for i in range(len(rock[0])):
                    if self.stack[h][x+i] != '#':
                        self.stack[h][x+i] = rock[l][i]
                h, l = h - 1, l - 1
            
            while l >= 0:
                self.stack.appendleft(list('#.......#'))
                for i in range(len(rock[0])):
                    self.stack[0][x+i] = rock[l][i]
                l -= 1
            
            self.last_element = len(self.stack)
            i = 0
            while self.stack[i] == list('#.......#'):
                self.last_element -= 1
                i += 1

        result1 = self.last_element - 1

        return result1, result2


solver = Solution("2022/q17.txt")
print(solver.solve())
