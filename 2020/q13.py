from math import gcd

class Solution:
    def __init__(self):
        pass
    
    def solve(self, filepath):
        f = open(filepath, 'r')
        result1, result2 = 0, 0
        lines = list()

        for line in f.readlines():
            lines.append(line)

        timestamp = int(lines[0])
        sched = lines[1].split(',')
        validSched = [(i, int(x)) for i, x in enumerate(sched) if x != 'x']
        
        # PART 1
        nextTime = list()
        minTime = 10**10
        for _, t in validSched:
            waitTime = t - (timestamp % t)
            if waitTime < minTime:
                minTime = waitTime
                result1 = waitTime*t

        # PART 2
        lcm = 1
        for (i,x) in validSched:
            while ((result2 + i) % x) != 0:
                result2 += lcm 
            lcm = lcm*x // gcd(lcm, x)

        return result1, result2

solver = Solution()
print(solver.solve('2020/q13.txt'))
