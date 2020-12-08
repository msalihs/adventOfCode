class Solution:
    def __init__(self):
        pass

    def solve(self, filepath, target):
        f = open(filepath, 'r')
        result = 0
        nums = list()
        result = list()
        for line in f.readlines():
            nums.append(int(line))
        additions = dict()
        for i, x in enumerate(nums):
            for y in nums[i+1:]:
                additions[x+y] = (x, y)
        
        for x in nums:
            if (target - x) in nums:
                result.append(target*x - x**2) 

        for x in nums:
            if (target - x) in additions:
                result.append(x * additions[target-x][0] * additions[target-x][1])
        return result   

solver = Solution()
print(solver.solve('2020/q1.txt', 2020))
