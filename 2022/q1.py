import heapq

class Solution:
    def __init__(self):
        pass

    def solve(self, filepath, target):
        f = open(filepath, 'r')
        result1, result2 = 0, 0
        elf_cals = [[]]
        for line in f.readlines():
            line = line.strip("\n")
            if line:
                elf_cals[-1].append(int(line))
            else:
                elf_cals.append([])

        for calories in elf_cals:
            result1 = max(result1, sum(calories))

        top_three = list()
        for calories in elf_cals:
            _sum = sum(calories)
            if len(top_three) < 3:
                heapq.heappush(top_three, _sum)
            elif _sum > top_three[0]:
                heapq.heappop(top_three)
                heapq.heappush(top_three, _sum)
                
        result2 = sum(top_three)

        return result1, result2

solver = Solution()
print(solver.solve('2022/q1.txt', 2020))
