import heapq

class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, 'r')
        result1, result2 = 0, 0

        rucksacks = []
        for line in f.readlines():
            line = line.strip("\n")
            rucksacks.append(line)

        priorities = {chr(ord('a') + i):i+1 for i in range(26)}
        for i in range(26):
            priorities[chr(ord('A')+i)] = 27 + i

        for items in rucksacks:
            m = len(items)//2
            left = set(items[0:m])
            right = set(items[m:])
            common = (right & left).pop()
            result1 += priorities[common]

        i = 0
        while i < len(rucksacks):
            common = (set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2])).pop()
            result2 += priorities[common]
            i += 3

        return result1, result2

solver = Solution()
print(solver.solve('2022/q3.txt'))
