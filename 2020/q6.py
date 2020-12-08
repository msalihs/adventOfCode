class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, 'r')
        result1, result2 = 0, 0

        inFile = [l.rstrip('\n') for l in f.read().split('\n\n')]
        
        # Part 1
        for groups in inFile:
            answers = set()
            for c in groups:
                if 'a' <= c <= 'z': answers.add(c)
            result1 += len(answers)

        # Part 2
        for groups in inFile:
            common = set([c for c in 'abcdefghijklmnopqrstuvwxyz'])
            for group in groups.split('\n'):
                common &= set([c for c in group])
            result2 += len(common)

        return result1, result2 

solver = Solution()
print(solver.solve('2020/q6.txt'))
