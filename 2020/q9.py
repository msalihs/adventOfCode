class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, 'r')
        result1, result2, found = 0, 0, False
        inFile = list()
        nums = list()

        for line in f.readlines():
            nums.append(int(line.strip('\n')))
        
        curr = set(nums[0:25])
        i = 25

        while i < len(nums):
            target = nums[i]
            for x in curr:
                if (target - x) in curr: break
            else:
                result1 = target
                break
            curr.remove(nums[i-25])
            curr.add(target)
            i += 1
        
        # Not ideal but small input space. Runs O(n3)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                subSum = sum(nums[i:j+1])
                if subSum == target:
                    result2 = min(nums[i:j]) + max(nums[i:j])
    
        return result1, result2

solver = Solution()
print(solver.solve('2020/q9.txt'))
