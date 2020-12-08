class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, 'r')
        result1, result2 = 0, 0
        
        for line in f.readlines():
            x = line.strip('\n').split(' ')
            if len(x) == 3:
                lb, ub = x[0].split('-')
                c = x[1][0]
                count = 0
                for d in x[2]:
                    if d == c: count += 1
                if int(lb) <= count <= int(ub):
                    result1 += 1
                if (x[2][int(lb)-1] == c) ^ (x[2][int(ub)-1] == c):
                    result2 += 1
        

        return result1, result2 

solver = Solution()
print(solver.solve('2020/q2.txt'))
