import math
class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, 'r')
        result1, result2 = 0, 0
        directives = list()
        m = {'N':(0,1), 'S':(0, -1), 'E':(1,0), 'W':(-1, 0)}

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
            if c in m:
                p[0] += m[c][0]*v
                p[1] += m[c][1]*v
            elif c == 'L' or c=='R':
                # https://en.wikipedia.org/wiki/Rotation_matrix
                if c=='R': v *= -1
                cos, sin = math.cos(math.radians(v)), math.sin(math.radians(v))
                d = [d[0]*cos - d[1]*sin, d[0]*sin + d[1]*cos]

        result1 = abs(round(p[0])) + abs(round(p[1]))

        # PART 2
        d = [10, 1]
        p = [0, 0]
        for c, v in directives:
            if c == 'F':
                p[0] += d[0]*v
                p[1] += d[1]*v
            if c in m:
                d[0] += m[c][0]*v
                d[1] += m[c][1]*v
            elif c == 'L' or c=='R':
                # https://en.wikipedia.org/wiki/Rotation_matrix
                if c=='R': v *= -1
                cos, sin = math.cos(math.radians(v)), math.sin(math.radians(v))
                d = [d[0]*cos - d[1]*sin, d[0]*sin + d[1]*cos]

        result2 = abs(round(p[0])) + abs(round(p[1]))
        

        return result1, result2

solver = Solution()
print(solver.solve('2020/q12.txt'))
