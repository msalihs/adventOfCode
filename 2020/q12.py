import math
class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, 'r')
        result1, result2 = 0, 0
        directives = list()

        for line in f.readlines():
            l = line.strip('\n')
            directives.append((l[0],int(l[1:])))

        # PART 1 
        d = [1, 0]
        p = [0, 0]
        for c, v in directives:
            if c == 'F':
                p[0] += d[0]*v
                p[1] += d[1]*v
            elif c == 'N':
                p[1] += v
            elif c == 'S':
                p[1] -= v
            elif c == 'E':
                p[0] += v
            elif c == 'W':
                p[0] -= v
            elif c == 'L' or c=='R':
                # https://en.wikipedia.org/wiki/Rotation_matrix
                if c=='R': v *= -1
                cos, sin = math.cos(math.radians(v)), math.sin(math.radians(v))
                d = [d[0]*cos - d[1]*sin, d[0]*sin + d[1]*cos]

        result1 = abs(p[0]) + abs(p[1])

        # PART 2
        d = [10, 1]
        p = [0, 0]
        for c, v in directives:
            if c == 'F':
                p[0] += d[0]*v
                p[1] += d[1]*v
            elif c == 'N':
                d[1] += v
            elif c == 'S':
                d[1] -= v
            elif c == 'E':
                d[0] += v
            elif c == 'W':
                d[0] -= v
            elif c == 'L' or c=='R':
                # https://en.wikipedia.org/wiki/Rotation_matrix
                if c=='R': v *= -1
                cos, sin = math.cos(math.radians(v)), math.sin(math.radians(v))
                d = [d[0]*cos - d[1]*sin, d[0]*sin + d[1]*cos]

        result2 = abs(p[0]) + abs(p[1])
        

        return result1, result2

solver = Solution()
print(solver.solve('2020/q12.txt'))
