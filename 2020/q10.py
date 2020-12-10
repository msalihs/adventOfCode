class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, 'r')
        result1, result2, found = 0, 0, False
        jolts = list()

        for line in f.readlines():
            jolts.append(int(line.strip('\n')))
        
        jolts.append(0)
        jolts.append(max(jolts) + 3)
        jolts.sort()
        
        diffs = dict()
        for i in range(1, len(jolts)):
            diff = jolts[i]-jolts[i-1]
            diffs[diff] = diffs.get(diff, 0) + 1
        result1 = diffs[1] * diffs[3]

        dp = dict()
        for x in jolts:
            if x == 0: dp[0] = 1 # Start condition
            else: dp[x] = dp.get(x-1, 0) + dp.get(x-2, 0) + dp.get(x-3, 0)
        
        result2 = dp[max(jolts)]    

        return result1, result2

solver = Solution()
print(solver.solve('2020/q10.txt'))
